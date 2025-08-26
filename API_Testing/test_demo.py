
"""  the process of passing a payload from a JSON file to a POST request """

import requests
import pytest

def test_get_validation():
    head = {
    "Content-Type": "application/json"
    }
    base_url = 'https://reqres.in/'
    response = requests.get(url=base_url + 'api/users/2', headers=head)
    assert response.status_code == 200
    print(response.text)
