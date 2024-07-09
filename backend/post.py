import requests

# Define the URL of the API endpoint
url = 'http://127.0.0.1:8000/databaseUser/create/'

# Define the data payload for the POST request
data = {
    "userID": 81921111,
    "tutor": None,
    "email": "test@student.curtin.edu.au",
    "firstName": "Test",
    "lastName": "Case"
}

# Set the headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response from the server
print('Status Code:', response.status_code)
print('Response Body:', response.text)
