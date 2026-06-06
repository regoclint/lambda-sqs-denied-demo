# lambda-sqs-denied-demo

Demonstrates a Lambda function that fails to send a message to SQS due to missing IAM permissions, with a CloudWatch alarm on the error.

## Stack (`template.yml`)
- **SQS Queue** – `demo-blocked-queue`
- **Lambda** – `demo-sqs-denied` (no `sqs:SendMessage` permission)
- **CW Alarm** – triggers on any Lambda error

## CI/CD Pipeline (`pipeline.yml`)

Merge to `main` → EventBridge rule detects push → CodePipeline → CodeBuild packages SAM template → CloudFormation deploys stack.

### Deploy the pipeline

```bash
aws cloudformation deploy \
  --template-file pipeline.yml \
  --stack-name lambda-sqs-denied-pipeline \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
```
