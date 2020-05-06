"""utility functions."""
import json
import decimal


def load_body(body):
    """Load request body."""
    return json.loads(body)


def response_builder(status_code, body={}):
    """Generate api response."""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body, cls=DecimalEncoder)
    }


class DecimalEncoder(json.JSONEncoder):
    """JSON encoder."""

    def default(self, obj):
        """encoding."""
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
