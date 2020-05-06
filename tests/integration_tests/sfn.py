"""Utilities of Step Functions for integration tests."""
import boto3
import json


class SfnTestUtils():
    """Utilities of Step Functions for integration tests."""

    _resource = None

    @classmethod
    def get_resource(cls):
        """Get sfn object."""
        if SfnTestUtils._resource is None:
            SfnTestUtils._resource = boto3.client('stepfunctions')
        return SfnTestUtils._resource

    @classmethod
    def start(cls, arn, input={}):
        """Execute your statemachine."""
        return cls.get_resource().start_execution(
            stateMachineArn=arn,
            input=json.dumps(input)
        )['executionArn']

    @classmethod
    def describe(cls, arn):
        """Describe execution status."""
        return cls.get_resource().describe_execution(
            executionArn=arn
        )['status']
