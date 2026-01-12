import requests


BASE_URL = "https://fakestoreapi.com"

def test_api_can_be_called():
    response = requests.get(BASE_URL)
    assert response.status_code in (200, 301, 302, 404)

