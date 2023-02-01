import requests

# endpoint
endpoint = 'http://localhost:8000/api/product/10/delete/'

# get response
response = requests.delete(endpoint)


# check status code equal 204
print(response.status_code == 204)
