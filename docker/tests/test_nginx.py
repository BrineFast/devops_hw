import requests


class TestNginx:
    def test_get_request_should_return_ok(self):
        response = requests.get("http://localhost:80")
        assert response.status_code == 403

    def test_post_request_should_return_forbidden(self):
        response = requests.post("http://localhost:80", data={'key': 'value'})
        assert response.status_code == 405
