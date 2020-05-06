import os
import boto3

events = boto3.client('events')


def handler(event, context):
    events.put_events(
        Entries=[
            {
                'Source': os.environ['EVENT_SOURCE'],
                'DetailType': os.environ['EVENT_SOURCE'],
                'Detail': '{}',
                'EventBusName': os.environ['EVENT_BUS_NAME'],
            }
        ]
    )
