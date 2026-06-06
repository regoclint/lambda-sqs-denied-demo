import boto3, os, logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    queue_url = os.environ["QUEUE_URL"]
    logger.info("Handler invoked. RequestId: %s", context.aws_request_id)
    logger.info("Event: %s", event)
    logger.info("Attempting to send message to SQS queue: %s", queue_url)
    try:
        sqs = boto3.client("sqs", region_name="us-east-1")
        response = sqs.send_message(QueueUrl=queue_url, MessageBody="hello from lambda")
        logger.info("Message sent successfully. MessageId: %s", response["MessageId"])
        return {"status": "sent", "messageId": response["MessageId"]}
    except Exception as e:
        logger.error("Failed to send message to SQS: %s", str(e))
        raise
