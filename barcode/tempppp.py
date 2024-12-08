import requests

# Replace with your actual token
token = 'your_obtained_token_here'

# URL of the endpoint you want to access
url = 'http://127.0.0.1:8000/inspections/inspection/'

# Set the Authorization header
headers = {
    'Authorization': f'Bearer {token}'
}

# Make a GET request with the token
response = requests.get(url, headers=headers)

# Print the response
print(response.json())



{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMzcwNTQ1NCwiaWF0IjoxNzMzNjE5MDU0LCJqdGkiOiJlOWYwMmY1NjFjODM0ZDVjYjdiZjI1OWZkZTYzMWE4ZSIsInVzZXJfaWQiOjF9.ax5g_DAL8Opn-nOV3T5rPRErAMxSjXuyWK8t8BQnTOY",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzNjE5MzU0LCJpYXQiOjE3MzM2MTkwNTQsImp0aSI6IjJkYTk0Y2M5YTMzMTQ4ZmM5OGQyMGRhZDcxM2U5NzMyIiwidXNlcl9pZCI6MX0.VxqqQJpIyOSzG3afDS0K7Iw6-iIDisZUpufSenNyepk"
}
























# import requests

# # Replace with your actual username and password
# login_data = {
#     'username': 'reza',
#     'password': 'Reza1234@'
# }

# # URL to obtain token
# url = 'http://127.0.0.1:8000/api/token/'

# # Make a POST request to get the token
# response = requests.post(url, data=login_data)

# # Get the access token from the response
# token = response.json().get('access')

# print(token)



# import requests

# # Token obtained from token_request.py
# token = 'ZmQ2YmU3MDQxMGRhZWFhMTRjYTI5ZWUzNmM3IiwidXNlcl9pZCI6MX0.JTSvQ1XbiRuCkPYXcW9SUYgKkdo8yj4gOU8s6XZjU-M'

# # URL of the endpoint you want to access
# url = 'url = 'http://127.0.0.1:8000/inspections/inspection/'

# # Set the Authorization header
# headers = {
#     'Authorization': f'Bearer {token}'
# }

# # Make a GET request with the token
# response = requests.get(url, headers=headers)

# # Print the response
# print(response.json())
