# AWS Infrastructure & Deployment

## Resource Overview

The image pipeline runs on four AWS resources:

| Resource | Type | Purpose |
|----------|------|---------|
| `ImageProcessorFunction` | Lambda function | Processes images on upload |
| S3 event notification | Bucket trigger | Fires Lambda when objects are created |
| `ImageProcessorDLQ` | SQS queue | Captures failed invocations |
| `ImageProcessorFunctionRole` | IAM role | Scoped permissions for the Lambda |

Everything except the S3 trigger is defined in the SAM template and deployed as a CloudFormation stack.

## SAM Template Walkthrough

The template lives at `lambda/template.yaml`. SAM (Serverless Application Model) is a CloudFormation superset purpose-built for Lambda. It was chosen over alternatives because:

- Simplest option for a single Lambda + trigger
- No state files to manage (unlike Terraform)
- No CDK boilerplate
- Two commands: `sam build` + `sam deploy`
- Template lives in the repo alongside the code

### Resources

**`ImageProcessorDLQ`** — SQS queue with 14-day message retention. When the Lambda fails all retry attempts, the event gets sent here instead of being lost. Check this queue when debugging missing images.

**`ImageProcessorFunction`** — The Lambda function itself. Key properties:

| Setting | Value | Why |
|---------|-------|-----|
| Runtime | `python3.12` | Latest stable Python runtime |
| Memory | 1024 MB | Large TIFFs and medium-format scans need room |
| Timeout | 120 seconds | Large files need time to download, process, and upload |
| Ephemeral storage | 1024 MB | `/tmp` space for large source files |
| Reserved concurrency | 10 | Prevents runaway invocations on bulk uploads |
| Retry attempts | 2 | Try twice more before sending to DLQ |

The function uses a `DeadLetterQueue` policy pointing to the SQS queue, so failed invocations are captured automatically.

**IAM permissions** — SAM generates a role automatically. The template adds an S3 policy:

```yaml
Policies:
  - S3CrudPolicy:
      BucketName: made-by-carson-images
```

This grants read/write to the specific bucket only. No `s3:*` wildcards.

### Outputs

The template exports `ImageProcessorFunctionArn` — needed by `setup_s3_trigger.sh` to wire the S3 event notification.

## S3 Trigger Wiring

**Why it's a separate step:** SAM can create S3 event triggers, but only for buckets it also creates. Since `made-by-carson-images` already exists, SAM can't attach events to it directly. The workaround is:

1. Deploy the Lambda via SAM (creates the function + IAM + DLQ)
2. Run `setup_s3_trigger.sh` to call `aws s3api put-bucket-notification-configuration`
3. The script also adds a Lambda resource-based policy (`aws lambda add-permission`) so S3 is allowed to invoke the function

This only needs to happen once. After that, any object created in the bucket will trigger the Lambda.

The trigger fires on `s3:ObjectCreated:*` — covers `PUT`, `POST`, multipart upload completion, and `COPY`.

## Deployment Steps

### Prerequisites

- AWS CLI configured with credentials (`aws configure`)
- SAM CLI installed (`brew install aws-sam-cli`)
- Docker running (SAM builds Pillow inside a Linux container to match Lambda's architecture)

### First-Time Deploy

```bash
cd lambda

# Build the Lambda package (compiles Pillow for Linux)
make build

# Deploy to AWS (interactive first time — sets stack name, region, confirms)
make deploy

# Wire S3 events to the Lambda (one-time)
make setup-trigger
```

On first `sam deploy --guided`, you'll be prompted for:
- Stack name → `image-processor`
- Region → `us-east-1` (or wherever your bucket is)
- Confirm changeset → yes

SAM saves these choices to `samconfig.toml` so subsequent deploys are non-interactive.

### Updating the Lambda

**Code changes** (modifying `app.py`):

```bash
cd lambda
make build && make deploy
```

**Config changes** (memory, timeout, etc.): edit `template.yaml`, then same build + deploy.

**Adding Python dependencies**: add to `requirements.txt`, then build + deploy. SAM handles packaging.

## Monitoring

### CloudWatch Logs

Every Lambda invocation writes to CloudWatch Logs under `/aws/lambda/image-processor-ImageProcessorFunction-*`. Each invocation logs:
- The S3 key being processed
- Whether it was skipped (not in `/original/`, unsupported extension)
- What outputs were generated
- Any errors

```bash
# Tail live logs
sam logs -n ImageProcessorFunction --stack-name image-processor --tail
```

### Dead Letter Queue

Check the DLQ for failed events:

```bash
aws sqs receive-message \
  --queue-url $(aws sqs get-queue-url --queue-name image-processor-ImageProcessorDLQ --query 'QueueUrl' --output text) \
  --max-number-of-messages 10
```

Common failure causes:
- Image is corrupted or truncated
- Unsupported format that Pillow can't open
- File exceeds ephemeral storage (1 GB)

### What to Check When Images Are Missing

1. Was the file uploaded to `original/`? (not the root folder)
2. Is the extension supported? (`.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.webp`)
3. Check CloudWatch logs for the invocation
4. Check DLQ for the failed event
5. Try re-uploading the file — the Lambda is idempotent

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

## GitHub Action Safety Net

`.github/workflows/lqip-generator.yml` runs the `scripts/lqip_generator.py` backfill script:

- **On push to main** (when `_posts/` changes) — catches cases where new posts reference images
- **Weekly schedule** (Sunday 6am UTC) — catches direct S3 uploads that the Lambda might have missed
- **Manual trigger** — process a specific folder on demand

The Action uses repository secrets for AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).

After confirming the Lambda is working reliably, the schedule can be reduced to monthly or removed entirely.

## File Inventory

```
lambda/
├── template.yaml                 # SAM infrastructure-as-code
├── Makefile                      # build, deploy, setup-trigger shortcuts
├── setup_s3_trigger.sh           # One-time: wires S3 events → Lambda
├── image_processor/
│   ├── __init__.py               # Package marker
│   ├── app.py                    # Lambda handler (all processing logic)
│   └── requirements.txt          # Pillow dependency
└── events/
    └── test_event.json           # For local testing with sam local invoke
```
