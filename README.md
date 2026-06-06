# lambda-sqs-denied-demo

Demonstrates a Lambda function that fails to send a message to SQS due to missing IAM permissions, with a CloudWatch alarm on the error.

## CI/CD Pipeline (`pipeline.yml`)

Merge to `main` → EventBridge rule detects push → CodePipeline → CodeBuild packages SAM template → CloudFormation deploys stack.

<!-- webhook test 3 -->
