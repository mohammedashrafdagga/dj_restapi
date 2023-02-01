import requests


# endpoint -  get all list
endpoint = 'http://localhost:8000/api/product/'


# get response
response = requests.get(endpoint)

# print json
print(response.json())
