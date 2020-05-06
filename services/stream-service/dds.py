"""DynamoDB Sreams backed Lambda."""
import os
import json
import boto3


kinesis = boto3.client('kinesis')


def handler(event, context):
    """DynamoDB Sreams backed Lambda."""
    for record in event['Records']:
        kinesis.put_record(
            StreamName=os.environ['STREAM_NAME'],
            Data=json.dumps(record),
            PartitionKey='uuid',
        )
