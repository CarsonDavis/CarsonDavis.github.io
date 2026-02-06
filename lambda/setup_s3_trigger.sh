#!/usr/bin/env bash
#
# One-time setup: wire S3 ObjectCreated events on the existing bucket
# to both Lambda functions. SAM can't do this for existing buckets.
#
# Triggers:
#   - /original/* -> ImageCompressorFunction
#   - /webp/*     -> LqipGeneratorFunction
#
# Prerequisites:
#   - Lambda deployed via `make deploy`
#   - AWS CLI configured with credentials
#
set -euo pipefail

BUCKET="made-by-carson-images"
STACK_NAME="image-processor"
REGION="${AWS_REGION:-us-east-1}"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Get Lambda ARNs from CloudFormation stack outputs
COMPRESSOR_ARN=$(aws cloudformation describe-stacks \
  --stack-name "$STACK_NAME" \
  --query 'Stacks[0].Outputs[?OutputKey==`ImageCompressorFunctionArn`].OutputValue' \
  --output text \
  --region "$REGION")

LQIP_ARN=$(aws cloudformation describe-stacks \
  --stack-name "$STACK_NAME" \
  --query 'Stacks[0].Outputs[?OutputKey==`LqipGeneratorFunctionArn`].OutputValue' \
  --output text \
  --region "$REGION")

if [ -z "$COMPRESSOR_ARN" ] || [ -z "$LQIP_ARN" ]; then
  echo "ERROR: Could not find Lambda ARNs. Is the stack deployed?"
  exit 1
fi

echo "Bucket:         $BUCKET"
echo "Compressor ARN: $COMPRESSOR_ARN"
echo "LQIP ARN:       $LQIP_ARN"
echo "Region:         $REGION"
echo ""

# Step 1: Grant S3 permission to invoke both Lambdas
echo "Adding S3 invoke permissions to Lambdas..."

aws lambda add-permission \
  --function-name "$COMPRESSOR_ARN" \
  --statement-id "s3-trigger-permission" \
  --action "lambda:InvokeFunction" \
  --principal "s3.amazonaws.com" \
  --source-arn "arn:aws:s3:::$BUCKET" \
  --source-account "$ACCOUNT_ID" \
  --region "$REGION" \
  2>/dev/null || echo "(Compressor permission may already exist — continuing)"

aws lambda add-permission \
  --function-name "$LQIP_ARN" \
  --statement-id "s3-trigger-permission" \
  --action "lambda:InvokeFunction" \
  --principal "s3.amazonaws.com" \
  --source-arn "arn:aws:s3:::$BUCKET" \
  --source-account "$ACCOUNT_ID" \
  --region "$REGION" \
  2>/dev/null || echo "(LQIP permission may already exist — continuing)"

# Step 2: Configure S3 bucket notifications for both functions
echo "Configuring S3 event notifications..."
aws s3api put-bucket-notification-configuration \
  --bucket "$BUCKET" \
  --notification-configuration "{
    \"LambdaFunctionConfigurations\": [
      {
        \"Id\": \"CompressorTrigger\",
        \"LambdaFunctionArn\": \"$COMPRESSOR_ARN\",
        \"Events\": [\"s3:ObjectCreated:*\"],
        \"Filter\": {
          \"Key\": {
            \"FilterRules\": [
              {\"Name\": \"prefix\", \"Value\": \"\"},
              {\"Name\": \"suffix\", \"Value\": \"\"}
            ]
          }
        }
      },
      {
        \"Id\": \"LqipGeneratorTrigger\",
        \"LambdaFunctionArn\": \"$LQIP_ARN\",
        \"Events\": [\"s3:ObjectCreated:*\"],
        \"Filter\": {
          \"Key\": {
            \"FilterRules\": [
              {\"Name\": \"prefix\", \"Value\": \"\"},
              {\"Name\": \"suffix\", \"Value\": \"\"}
            ]
          }
        }
      }
    ]
  }" \
  --region "$REGION"

echo ""
echo "Done. S3 events on '$BUCKET' will now trigger both Lambdas."
echo ""
echo "Test new post workflow:"
echo "  aws s3 cp test.jpg s3://$BUCKET/test-folder/original/test.jpg"
echo ""
echo "Test migration workflow:"
echo "  aws s3 cp existing.webp s3://$BUCKET/test-folder/webp/existing.webp"
