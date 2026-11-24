import requests
import json

API_URL = "https://events.purdue.edu/api/2/events?days=7&pp=100" # Fetches events for the next seven days

response = requests.get(API_URL)
data = response.json()

print(data['events'][0])

events = data['events']

filtered_events = []
filtered_events_titles = []

## TODO: Check other fields; format the keyword word search
for event in events:
    if "Men".lower() in event['event']['title'].lower(): 
        # print(event['event'])
        # filtered_events.append(event['event'])
        filtered_events_titles.append(event['event']['title'])

print(filtered_events_titles)