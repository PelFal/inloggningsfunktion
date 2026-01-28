import requests
import pytest

pytestmark = pytest.mark.api


BASE_URL = "https://fakestoreapi.com/products"

def test_api_can_be_called_200():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

