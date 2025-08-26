import requests

head = {
    "Accept": "text/plain",
    "Content-Type": "application/json"
}
request_payload = {
"id": 190,
"title": "Api testing request 2",
"dueDate": "2025-03-16T14:28:35.605Z",
"completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                         headers=head, json=request_payload)
print(response.status_code)
print(response.json())
data = response.json()

assert response.status_code == 200
assert data['id'] == 190
assert data['completed'] == True
