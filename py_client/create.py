import requests

from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'

password = getpass()

auth_response = requests.post(
    auth_endpoint, json={'username': 'staff', 'password': password})

if auth_response.status_code == 200:
    # get token
    token = auth_response.json()['token']

    # data saved
    data = {'title': 'Python Request',
            'price': 32.22}
    # endpoint
    endpoint = 'http://localhost:8000/api/product/'

    # headers
    headers = {'Authorization': f'Bearer {token}'}

    # get response
    response = requests.post(endpoint, json=data, headers=headers)

    # print json
    print(response.json())
