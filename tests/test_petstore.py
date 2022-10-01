import requests
import pytest

def test_status_code():
    url = 'https://petstore.swagger.io/v2/pet/1'
    response = requests.get(url)
    assert response.status_code == 200

def test_pet_name():
    url = 'https://petstore.swagger.io/v2/pet/1'
    response = requests.get(url)
    response = response.json()
    assert response['name'] == 'Lucio'