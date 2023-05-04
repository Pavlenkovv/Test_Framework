import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print("==================================================================")
    print(f"Status code is: {r.status_code}")
    print("==================================================================")
    print(f"Response is: {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/pavlenkovv')
    print(f"Response Body is: {r.json()}")
    print("==================================================================")
    print(f"Response status code is: {r.status_code}")
    print("==================================================================")
    print(f"Response Headers is: {r.headers}")


@pytest.mark.http
def test_third_request():
    r = requests.get('https://api.github.com/events')
    print(f"Response is: {r.text}")
