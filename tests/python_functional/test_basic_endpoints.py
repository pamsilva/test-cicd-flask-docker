import requests


def test_root():
    response = requests.get('http://localhost:5000')
    assert response.status_code == 200


def test_hello():
    response = requests.get('http://localhost:5000/hello')
    assert response.status_code == 200


def test_get_items():
    response = requests.get('http://localhost:5000/items')
    assert response.status_code == 200
