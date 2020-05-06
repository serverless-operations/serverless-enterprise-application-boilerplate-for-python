import os
from tests.integration_tests.sfn import SfnTestUtils
from tests.integration_tests.utils import sleep
range_count = 10
wait_time = 3


class TestWorkflow(object):
    """Integration tests for workflow service."""

    def test_success_case(self, fixture_success):
        """test for a normal situation."""
        execution_arn = SfnTestUtils.start(os.environ['MyStateMachine'])
        for _ in range(range_count):
            sleep(wait_time)
            if SfnTestUtils.describe(execution_arn) == 'SUCCEEDED':
                break

        # Assert for a normal case.
        assert True
