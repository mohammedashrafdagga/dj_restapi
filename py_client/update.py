import requests

# endpoint
endpoint = 'http://localhost:8000/api/product/12/update/'


data = {'title': 'Hello Python', 'price': '12.33'}
# get response
response = requests.put(endpoint, json=data)


# check update
print(response.json())
