import os
import pytest
from tests.integration_tests.utils import set_table_names
from tests.integration_tests.utils import get_endpoint_url
service = 'api'


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    """Set table name to environment valiables."""
    set_table_names(os.environ['STAGE'])
    yield


@pytest.fixture(scope='module', autouse=True)
def endpoint():
    """Pass API Gateway endpoint URL."""
    yield(get_endpoint_url(service, os.environ['STAGE']))
