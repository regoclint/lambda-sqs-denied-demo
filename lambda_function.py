import boto3

def handler(event, context):
    sqs = boto3.client("sqs", region_name="us-east-1")
    queue_url = "https://sqs.us-east-1.amazonaws.com/314820560132/demo-blocked-queue"
    sqs.send_message(QueueUrl=queue_url, MessageBody="hello from lambda")
    return {"status": "sent"}
