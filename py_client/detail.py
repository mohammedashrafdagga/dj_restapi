import requests

from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'

password = getpass()

auth_response = requests.post(
    auth_endpoint, json={'username': 'staff', 'password': password})

if auth_response.status_code == 200:
    # get token
    token = auth_response.json()['token']

    # endpoint
    endpoint = 'http://localhost:8000/api/product/12/'

    # headers
    headers = {'Authorization': f'Bearer {token}'}

    # get response
    response = requests.get(endpoint, headers=headers)

    # print json
    print(response.json())

