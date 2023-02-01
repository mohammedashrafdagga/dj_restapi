import requests

# endpoint
endpoint = 'http://localhost:8000/api/product/12/'


# get response
response = requests.get(endpoint)

# print json
print(response.json())
