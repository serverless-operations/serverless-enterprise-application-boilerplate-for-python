import os
import pytest
from tests.integration_tests.utils import set_table_names, set_sfn_arn, set_s3_bucket_names


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    """Set some resources info to environment valiables."""
    set_table_names(stage=os.environ['STAGE'])
    set_sfn_arn('workflow', stage=os.environ['STAGE'])
    set_s3_bucket_names(stage=os.environ['STAGE'])


@pytest.fixture
def fixture_success():
    # Write process before runing test
    yield
    # After process before runing test
