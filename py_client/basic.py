import requests


# create endpoint
endpoint = 'https://httpbin.org/anything'


# send request
get_response = requests.get(endpoint)

# get json from response
print(get_response.json())

# status code
print(get_response.status_code)
