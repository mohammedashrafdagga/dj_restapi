import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'

password = getpass()

auth_response = requests.post(
    auth_endpoint, json={'username': 'staff', 'password': password})

# print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()['token']

    # endpoint -  get all list
    endpoint = 'http://localhost:8000/api/product/'

    # headers
    headers = {'Authorization': f'Bearer {token}'}

    # get response
    response = requests.get(endpoint, headers=headers)

    # print json
    print(response.json())
