import requests

param = {
    'page':3,
    'per_page':2
}
url="https://gorest.co.in/public/v2/users"
response = requests.get(url, params=param)
print(response.json())
assert response.status_code == 200