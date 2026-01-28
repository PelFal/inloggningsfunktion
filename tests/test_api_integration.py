import requests
import pytest

pytestmark = pytest.mark.api


BASE_URL = "https://fakestoreapi.com"

def test_api_can_be_called():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
#testmotgitubhactions