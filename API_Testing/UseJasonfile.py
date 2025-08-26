
"""  the process of passing a payload from a JSON file to a POST request """

import requests
import json

base_url= 'https://reqres.in/api/users'
head = {
    "Content-Type": "application/json"
}
json_file= open('users.json')
json_data= json.load(json_file)
# json = json.dumps(json_data) we will use dumps to load csv or other files
response = requests.post(url=base_url, headers=head , json=json_data)
print(response.status_code)
#print(response.json())
print(response.text)
