import boto3
import os
import time


def sleep(seconds):
    """sleep for waiting end of async process."""
    time.sleep(seconds)


def get_endpoint_url(service_name, stage):
    """Get APIGateway endpoint URL."""
    cloudformation = boto3.client('cloudformation')
    stackname = '{}-{}'.format(service_name, stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )

    for output in response['Stacks'][0]['Outputs']:
        if output['OutputKey'] == 'ServiceEndpoint':
            return output['OutputValue']


def set_table_names(stage):
    """Set tablename to environment variables."""
    cloudformation = boto3.client('cloudformation')
    stackname = 'db-{}'.format(stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )

    for output in response['Stacks'][0]['Outputs']:
        os.environ[output.get('OutputKey')] = output.get('OutputValue')


def set_s3_bucket_names(stage):
    """Set S3 info to environment variables."""
    cloudformation = boto3.client('cloudformation')
    stackname = 's3-{}'.format(stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )

    for output in response['Stacks'][0]['Outputs']:
        os.environ[output.get('OutputKey')] = output.get('OutputValue')


def set_sfn_arn(service_name, stage):
    """Set Step Functions info to environment variables."""
    cloudformation = boto3.client('cloudformation')
    stackname = '{}-{}'.format(service_name, stage)
    response = cloudformation.describe_stacks(
        StackName=stackname
    )

    for output in response['Stacks'][0]['Outputs']:
        os.environ[output.get('OutputKey')] = output.get('OutputValue')
