import json
import boto3
import os

client = boto3.client('connect', region_name='XXX')

def lambda_handler(event, context):

    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber='XXX', # Customer's phone number
        ContactFlowId='XXX', # The Contact flow Id of the flow that you want to run
        InstanceId='XXX', # The Connect Instance Id
        SourcePhoneNumber='XXX', # The claimed Connect phone number
        Attributes={
            'prompt': 'This is an automated call from UnicornRestaurant, this is to remind you of an upcoming dining reservation in our restaurant today at 9 PM for 2 people.'
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
