import requests


class TestHello(object):

    def test_return_200_with_success(self, endpoint):
        """Should return 200 response."""
        response = requests.get(
            url=endpoint + '/hello',
            headers={
                'Content-Type': 'application/json'
            }
        )

        assert response.status_code == 200
