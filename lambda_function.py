import boto3, os

def handler(event, context):
    sqs = boto3.client("sqs", region_name="us-east-1")
    sqs.send_message(QueueUrl=os.environ["QUEUE_URL"], MessageBody="hello from lambda")
    return {"status": "sent"}
