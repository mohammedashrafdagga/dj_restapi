import requests


# create endpoint
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/'  # http://127.0.0.1:8000/


# send request
get_response = requests.get(endpoint)

# get text from application  response
# print(get_response.text)

# status code
print(get_response.status_code)
