# AWS Infrastructure & Deployment

## Resource Overview

The image pipeline runs on these AWS resources:

| Resource | Type | Purpose |
|----------|------|---------|
| `ImageCompressorFunction` | Lambda function | Converts originals to WebP |
| `LqipGeneratorFunction` | Lambda function | Creates 16px thumbnails |
| S3 event notifications | Bucket triggers | Fires Lambdas when objects are created |
| `CompressorDLQ` | SQS queue | Captures failed compressor invocations |
| `LqipGeneratorDLQ` | SQS queue | Captures failed LQIP generator invocations |

Everything except the S3 triggers is defined in the SAM template and deployed as a CloudFormation stack.

## SAM Template Walkthrough

The template lives at `lambda/template.yaml`. SAM (Serverless Application Model) is a CloudFormation superset purpose-built for Lambda. It was chosen over alternatives because:

- Simplest option for Lambda + triggers
- No state files to manage (unlike Terraform)
- No CDK boilerplate
- Two commands: `sam build` + `sam deploy`
- Template lives in the repo alongside the code

### Resources

**`CompressorDLQ` / `LqipGeneratorDLQ`** — SQS queues with 14-day message retention. When a Lambda fails all retry attempts, the event gets sent here instead of being lost. Check these queues when debugging missing images.

**`ImageCompressorFunction`** — Converts images from `original/` to WebP in `webp/`. Deployed as a container image with `cwebp` installed.

| Setting | Value | Why |
|---------|-------|-----|
| Package type | Container image | Allows installing system binaries like `cwebp` |
| Base image | `public.ecr.aws/lambda/python:3.12` | AWS-managed Lambda runtime |
| Memory | 1024 MB | Large TIFFs and medium-format scans need room |
| Timeout | 120 seconds | Large files need time to download, process, and upload |
| Ephemeral storage | 1024 MB | `/tmp` space for large source files |
| Reserved concurrency | 10 | Prevents runaway invocations on bulk uploads |
| Retry attempts | 2 | Try twice more before sending to DLQ |

**`LqipGeneratorFunction`** — Creates 16px thumbnails from WebPs in `webp/`, writes to `lqip/`. Uses the same container image but with a different handler.

| Setting | Value | Why |
|---------|-------|-----|
| Memory | 512 MB | Thumbnails are lightweight |
| Ephemeral storage | 512 MB | Only downloading small WebPs |
| Other settings | Same as compressor | — |

Both functions use a `DeadLetterQueue` policy pointing to their respective SQS queues.

**IAM permissions** — SAM generates a role automatically. The template adds an S3 policy:

```yaml
Policies:
  - S3CrudPolicy:
      BucketName: made-by-carson-images
```

This grants read/write to the specific bucket only. No `s3:*` wildcards.

### Outputs

The template exports `ImageCompressorFunctionArn` and `LqipGeneratorFunctionArn` — needed by `setup_s3_trigger.sh` to wire the S3 event notifications.

## S3 Trigger Wiring

**Why it's a separate step:** SAM can create S3 event triggers, but only for buckets it also creates. Since `made-by-carson-images` already exists, SAM can't attach events to it directly. The workaround is:

1. Deploy the Lambdas via SAM (creates the functions + IAM + DLQs)
2. Run `setup_s3_trigger.sh` to call `aws s3api put-bucket-notification-configuration`
3. The script also adds Lambda resource-based policies (`aws lambda add-permission`) so S3 is allowed to invoke both functions

This only needs to happen once. After that, any object created in the bucket will trigger the appropriate Lambda.

Both triggers fire on `s3:ObjectCreated:*` — covers `PUT`, `POST`, multipart upload completion, and `COPY`. The Lambdas themselves filter by path (`/original/` vs `/webp/`).

## CI/CD Deployment

The Lambda is deployed automatically via GitHub Actions when changes are pushed to `lambda/` on `main`.

**Workflow:** `.github/workflows/lambda-deploy.yml`

**Triggers:**
- Push to `main` that changes any file in `lambda/`
- Manual trigger via workflow_dispatch

**What it does:**
1. Checks out the repo
2. Sets up Python 3.12 and SAM CLI
3. Authenticates to AWS via OIDC (no static credentials)
4. Runs `sam build` (builds the container image)
5. Runs `sam deploy` (pushes to ECR, updates CloudFormation stack)

### First-Time Setup (One-Time)

Before CI/CD will work, you need to set up OIDC authentication between GitHub and AWS.

#### 1. Create the GitHub OIDC Identity Provider in AWS

```bash
aws iam create-open-id-connect-provider \
  --url https://token.actions.githubusercontent.com \
  --client-id-list sts.amazonaws.com \
  --thumbprint-list 6938fd4d98bab03faadb97b34396831e3780aea1
```

#### 2. Create the IAM Role

Create a file `github-actions-trust-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:CarsonDavis/CarsonDavis.github.io:*"
        }
      }
    }
  ]
}
```

Replace `ACCOUNT_ID` with your AWS account ID, then create the role:

```bash
aws iam create-role \
  --role-name github-actions-role \
  --assume-role-policy-document file://github-actions-trust-policy.json
```

#### 3. Attach Permissions to the Role

The role needs permissions for SAM deployments and S3 access:

```bash
# CloudFormation and SAM deployment permissions
aws iam attach-role-policy \
  --role-name github-actions-role \
  --policy-arn arn:aws:iam::aws:policy/AWSCloudFormationFullAccess

aws iam attach-role-policy \
  --role-name github-actions-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess

aws iam attach-role-policy \
  --role-name github-actions-role \
  --policy-arn arn:aws:iam::aws:policy/AWSLambda_FullAccess

aws iam attach-role-policy \
  --role-name github-actions-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess

aws iam attach-role-policy \
  --role-name github-actions-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

aws iam attach-role-policy \
  --role-name github-actions-role \
  --policy-arn arn:aws:iam::aws:policy/IAMFullAccess
```

#### 4. Add Repository Secret

In your GitHub repo, go to Settings → Secrets and variables → Actions, and add:

- `AWS_ACCOUNT_ID`: Your 12-digit AWS account ID

#### 5. Wire the S3 Trigger

After the first CI/CD deploy completes:

```bash
cd lambda
make setup-trigger
```

This only needs to happen once. After that, pushes to `lambda/` deploy automatically.

### Local Development

For testing changes locally before pushing:

```bash
cd lambda
make build                    # Build container image
make test-compressor          # Test compressor with sample event
make test-lqip                # Test LQIP generator with sample event

# Watch logs
sam logs -n ImageCompressorFunction --stack-name image-processor --tail
sam logs -n LqipGeneratorFunction --stack-name image-processor --tail
```

### Making Changes

**Code changes** — edit files in `lambda/`, push to `main`. CI/CD deploys automatically.

**Config changes** (memory, timeout, etc.) — edit `template.yaml`, push to `main`.

**Python dependencies** — add to `requirements.txt`, push to `main`.

**System dependencies** — add to the `RUN dnf install` line in `image_processor/Dockerfile`, push to `main`.

## Monitoring

### CloudWatch Logs

Each Lambda writes to its own CloudWatch log group:
- `/aws/lambda/image-compressor`
- `/aws/lambda/lqip-generator`

Each invocation logs the S3 key being processed, whether it was skipped, what outputs were generated, and any errors.

```bash
# Tail live logs
sam logs -n ImageCompressorFunction --stack-name image-processor --tail
sam logs -n LqipGeneratorFunction --stack-name image-processor --tail
```

### Dead Letter Queues

Check the DLQs for failed events:

```bash
# Compressor failures
aws sqs receive-message \
  --queue-url $(aws sqs get-queue-url --queue-name image-processor-CompressorDLQ --query 'QueueUrl' --output text) \
  --max-number-of-messages 10

# LQIP generator failures
aws sqs receive-message \
  --queue-url $(aws sqs get-queue-url --queue-name image-processor-LqipGeneratorDLQ --query 'QueueUrl' --output text) \
  --max-number-of-messages 10
```

Common failure causes:
- Image is corrupted or truncated
- Unsupported format that `cwebp` or Pillow can't handle
- File exceeds ephemeral storage

### What to Check When Images Are Missing

**WebP missing (compressor issue):**
1. Was the file uploaded to `original/`?
2. Is the extension supported? (`.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.webp`)
3. Check compressor CloudWatch logs
4. Check compressor DLQ

**LQIP missing (generator issue):**
1. Does the WebP exist in `webp/`?
2. Check LQIP generator CloudWatch logs
3. Check LQIP generator DLQ

Both Lambdas are idempotent — re-uploading the source file will regenerate outputs.

## Cost

Effectively $0 for a personal blog.

| Resource | Free Tier | Typical Monthly Usage |
|----------|-----------|----------------------|
| Lambda invocations | 1M requests/month | ~50–100 |
| Lambda compute | 400K GB-seconds/month | ~50–100 GB-seconds |
| SQS | 1M requests/month | 0 (hopefully) |
| CloudWatch Logs | 5 GB ingestion/month | <1 MB |
| S3 storage | 5 GB (first year) | ~2 GB total |

Even outside the free tier, costs would be pennies per month.

## File Inventory

```
lambda/
├── template.yaml                 # SAM infrastructure-as-code
├── samconfig.toml                # Deploy configuration (stack name, region)
├── Makefile                      # build, test, setup-trigger shortcuts
├── setup_s3_trigger.sh           # One-time: wires S3 events → both Lambdas
├── image_processor/
│   ├── Dockerfile                # Container image: Python 3.12 + cwebp
│   ├── __init__.py               # Package marker
│   ├── app.py                    # Both handlers: compressor_handler, lqip_handler
│   └── requirements.txt          # Pillow, boto3
└── events/
    ├── compressor_test.json      # Test event for compressor
    └── lqip_test.json            # Test event for LQIP generator

.github/workflows/
└── lambda-deploy.yml             # CI/CD: deploys Lambdas on push to lambda/
```
