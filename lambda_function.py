import boto3, os, logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Attempting to send message to SQS queue: %s", os.environ["QUEUE_URL"])
    sqs = boto3.client("sqs", region_name="us-east-1")
    sqs.send_message(QueueUrl=os.environ["QUEUE_URL"], MessageBody="hello from lambda")
    return {"status": "sent"}
