import json
import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('demo-table2')

def hello(event, context):

    try:
        print('event:', event)

        records = event['Records']

        body = json.loads(records[0]['body'])

        # Log the body, which is the message
        print("Incoming message body from SQS:", body)

        # Write data to DynamoDB
        item = {
            'userId': body['userId'],
            'name': body['name'],
            'age': body['age']
        }

        response = table.put_item(Item=item)

        print('Successfully written to DynamoDB:', response)

    except Exception as e:
        print('Error in executing lambda:', e)
        return {"statusCode": 500, "message": "Error while execution"}

    return {"statusCode": 200, "message": "Successfully executed Lambda"}

