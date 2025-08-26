import requests

head = {
    "Accept": "text/plain"
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/13", headers=head)
print('Before Updating the data 12')
print(response.json())
assert response.status_code == 200

headput = {
    "Accept": "text/plain",
    "Content-Type": "application/json"
}
put_payload = {
    "id": 15,
    "title": "Api testing request 12 updated to 15",
    "dueDate": "2025-03-16T14:28:35.605Z",
    "completed": True
}

responsePut = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",
                        headers=headput, json=put_payload)
print('After Updating the data 12')
print(responsePut.json())
assert responsePut.status_code == 200

headdel = {"Content-Type": "application/json"}  # Modify if needed
responseDel = requests.delete("https://fakerestapi.azurewebsites.net/api/v1/Activities/13",
                              headers=headdel )
# Print debug information
print("DELETE Status Code:", responseDel.status_code)
print("DELETE Response Body:", responseDel.text)

# Check if the deletion was successful
if responseDel.status_code == 200:
    print("Successfully deleted ID 13.")
else:
    print("Failed to delete. Possible reasons: ID does not exist, auth required, or API does not support DELETE.")
