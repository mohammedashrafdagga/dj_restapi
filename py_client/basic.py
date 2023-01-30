import requests


# create endpoint
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'  # http://127.0.0.1:8000/


# send request
get_response = requests.get(endpoint)

#  get Json from application  response
print(get_response.json())

# status code
print(get_response.status_code)

# print a message form json
print(get_response.json()['message'])
