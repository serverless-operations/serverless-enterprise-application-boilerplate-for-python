"""tests for utils.py."""
from unittest import TestCase
from lib.utils import load_body


class TestUtiles(TestCase):
    """tests for utils.py."""

    def test_load_body(self):
        """Should return dict type object."""
        assert load_body('{"a":"b"}') == {'a': 'b'}
