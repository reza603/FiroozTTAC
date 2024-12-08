import requests

# URL for the protected resource
url = "http://199.203.18.44:8000/inspections/api/inspection/"

# Headers with the Bearer token
headers = {
"Authorization": "Bearer 30590fde746f528c0dfe6175da2f1f49ed4de2af"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.status_code)
print(response.json())