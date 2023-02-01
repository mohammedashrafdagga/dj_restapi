import requests


# data saved
data = {'title': 'Python Request',
        'content': 'create from python request',
        'price': 32.22}
# endpoint
endpoint = 'http://localhost:8000/api/product/'


# get response
response = requests.post(endpoint, json=data)

# print json
print(response.json())
