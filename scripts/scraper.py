import requests
# import json

API_URL = "https://events.purdue.edu/api/2/events?days=7&pp=100" # Fetches events for the next seven days

response = requests.get(API_URL)
data = response.json()

print(data)
