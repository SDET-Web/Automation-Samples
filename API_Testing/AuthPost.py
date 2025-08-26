import requests

head= {
     "Content-Type": "application/json",
     "Authorization": "Bearer bc64493c11503b7d04aca956998b4e0ff9b0442d75c85059cfeb5a7b181b35a9" }

request_payload = {
    "id": 277522,
    "name": "Test APIS User",
    "email": "test2233_jha_ajit@gislasons.example",
    "gender": "female",
    "status": "active"
}

url= "https://gorest.co.in/public/v2/users"
response = requests.post(url, headers=head, json=request_payload)
#print(response.status_code)
print(response.json())
assert response.status_code == 201

get_response = requests.get(url+'/'+ str(response.json()['id']), headers=head)
print(get_response.json())
print(get_response.json()['email'])