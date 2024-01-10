import boto3
import json

def send_message_to_sqs():
   
    queue_url = 'https://sqs.us-east-1.amazonaws.com/054244991161/First-project-dev-my-queue'

    # Message to be sent
    message_body = {
        "userId": "678",
        "name": "Naveen Kushwaha",
        "age": 21
    }

    sqs = boto3.client('sqs',region_name='us-east-1')

    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message_body)
    )

    print(f"Message sent. MessageId: {response['MessageId']}")


send_message_to_sqs()
