#!/usr/bin/env bash
#
# One-time setup: wire S3 ObjectCreated events on the existing bucket
# to both Lambda functions via SNS fan-out. SAM can't attach events
# to existing buckets, and S3 won't allow two Lambda targets with
# overlapping filters, so we use an SNS topic as the intermediary.
#
# Flow: S3 ObjectCreated -> SNS topic -> both Lambdas
#
# The Lambdas filter internally by key path:
#   - Compressor handles keys matching */original/*
#   - LQIP Generator handles keys matching */webp/*
#
# Prerequisites:
#   - Lambda deployed via `make deploy`
#   - AWS CLI configured (uses AWS_PROFILE, default: personal)
#
set -euo pipefail

BUCKET="made-by-carson-images"
STACK_NAME="image-processor"
REGION="${AWS_REGION:-us-east-1}"
PROFILE="${AWS_PROFILE:-personal}"
TOPIC_NAME="image-processor-s3-events"

PROFILE_ARG=(--profile "$PROFILE")

ACCOUNT_ID=$(aws sts get-caller-identity "${PROFILE_ARG[@]}" --query Account --output text)

# Get Lambda ARNs from CloudFormation stack outputs
COMPRESSOR_ARN=$(aws cloudformation describe-stacks \
  "${PROFILE_ARG[@]}" \
  --stack-name "$STACK_NAME" \
  --query 'Stacks[0].Outputs[?OutputKey==`ImageCompressorFunctionArn`].OutputValue' \
  --output text \
  --region "$REGION")

LQIP_ARN=$(aws cloudformation describe-stacks \
  "${PROFILE_ARG[@]}" \
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
echo "Profile:        $PROFILE"
echo ""

# Step 1: Create SNS topic (idempotent — returns existing topic if it already exists)
echo "Creating SNS topic '$TOPIC_NAME'..."
TOPIC_ARN=$(aws sns create-topic \
  "${PROFILE_ARG[@]}" \
  --name "$TOPIC_NAME" \
  --region "$REGION" \
  --query 'TopicArn' \
  --output text)

echo "Topic ARN:      $TOPIC_ARN"

# Step 2: Allow S3 to publish to the SNS topic
echo "Setting SNS topic policy for S3 access..."
aws sns set-topic-attributes \
  "${PROFILE_ARG[@]}" \
  --topic-arn "$TOPIC_ARN" \
  --attribute-name Policy \
  --attribute-value "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Sid\": \"AllowS3Publish\",
      \"Effect\": \"Allow\",
      \"Principal\": {\"Service\": \"s3.amazonaws.com\"},
      \"Action\": \"sns:Publish\",
      \"Resource\": \"$TOPIC_ARN\",
      \"Condition\": {
        \"ArnLike\": {\"aws:SourceArn\": \"arn:aws:s3:::$BUCKET\"},
        \"StringEquals\": {\"aws:SourceAccount\": \"$ACCOUNT_ID\"}
      }
    }]
  }" \
  --region "$REGION"

# Step 3: Allow SNS to invoke both Lambdas
echo "Adding SNS invoke permissions to Lambdas..."

aws lambda add-permission \
  "${PROFILE_ARG[@]}" \
  --function-name "$COMPRESSOR_ARN" \
  --statement-id "sns-trigger-permission" \
  --action "lambda:InvokeFunction" \
  --principal "sns.amazonaws.com" \
  --source-arn "$TOPIC_ARN" \
  --region "$REGION" \
  2>/dev/null || echo "(Compressor SNS permission may already exist — continuing)"

aws lambda add-permission \
  "${PROFILE_ARG[@]}" \
  --function-name "$LQIP_ARN" \
  --statement-id "sns-trigger-permission" \
  --action "lambda:InvokeFunction" \
  --principal "sns.amazonaws.com" \
  --source-arn "$TOPIC_ARN" \
  --region "$REGION" \
  2>/dev/null || echo "(LQIP SNS permission may already exist — continuing)"

# Step 4: Subscribe both Lambdas to the SNS topic
echo "Subscribing Lambdas to SNS topic..."

aws sns subscribe \
  "${PROFILE_ARG[@]}" \
  --topic-arn "$TOPIC_ARN" \
  --protocol lambda \
  --notification-endpoint "$COMPRESSOR_ARN" \
  --region "$REGION"

aws sns subscribe \
  "${PROFILE_ARG[@]}" \
  --topic-arn "$TOPIC_ARN" \
  --protocol lambda \
  --notification-endpoint "$LQIP_ARN" \
  --region "$REGION"

# Step 5: Configure S3 to send ObjectCreated events to SNS
echo "Configuring S3 event notifications..."
aws s3api put-bucket-notification-configuration \
  "${PROFILE_ARG[@]}" \
  --bucket "$BUCKET" \
  --notification-configuration "{
    \"TopicConfigurations\": [
      {
        \"Id\": \"ImageProcessorEvents\",
        \"TopicArn\": \"$TOPIC_ARN\",
        \"Events\": [\"s3:ObjectCreated:*\"]
      }
    ]
  }" \
  --region "$REGION"

echo ""
echo "Done. S3 events on '$BUCKET' -> SNS '$TOPIC_NAME' -> both Lambdas."
echo ""
echo "Test new post workflow:"
echo "  aws s3 cp test.jpg s3://$BUCKET/test-folder/original/test.jpg --profile $PROFILE"
echo ""
echo "Test migration workflow:"
echo "  aws s3 cp existing.webp s3://$BUCKET/test-folder/webp/existing.webp --profile $PROFILE"
