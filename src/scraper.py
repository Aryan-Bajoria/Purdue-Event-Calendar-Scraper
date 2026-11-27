import requests
import json

"""
Scraper.py

Uses the Purdue Events Calendar API to fetch events from the next 7 days.
Finds your preferences from a config file.
Matches your preferences to the events.
Saves relevant events as a csv file on your desktop.
"""


## Add negative event type searches too, say if the user doesn't want to go to a certain type of event


def match_search(search_words, omit_event_types, omit_event_words, event, event_type = None, audience = None):
    searchable_fields = [
        event.get("title", ""),
        event.get("description", ""),
        event.get("description_text", "") #TODO: Check if needed/how its different to description

        filters = event.get("filters", {})
        event_types = filters.get("event_types", [])
        searchable
    ]



API_URL = "https://events.purdue.edu/api/2/events?days=7&pp=100" # Fetches events for the next seven days

response = requests.get(API_URL)
data = response.json()

# Use this to see the format of a single event fetched from the api.
# print(data['events'][0]) 

events = data['events']

filtered_events = []
filtered_events_titles = []

## TODO: Check other fields (consider description, filters); format the keyword word search

## Check all fields
## tags

search_word = "Men".lower()

# TODO: Compare description text and description

for event in events:
    if search_word in event['event']['title'].lower() or event['event']['description_text'].lower() or event['event']: 
        # print(event['event'])
        # filtered_events.append(event['event'])
        filtered_events_titles.append(event['event']['title'])

print(filtered_events_titles)
