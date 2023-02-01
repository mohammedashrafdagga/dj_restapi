import requests

# endpoint - for not found instance
endpoint = 'http://localhost:8000/api/product/500/'


# get response
response = requests.get(endpoint)

# print json
print(response.json())
