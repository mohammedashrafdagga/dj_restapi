import requests


# create endpoint
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'  # http://127.0.0.1:8000/


# send request
get_response = requests.post(
    endpoint, json={'title': 'abc123', 'content': 'Hello World', 'price': 15.15})

#  get Json from application  response
print(get_response.json())
