#!/usr/bin/env python
# wu_weather.py - Prints the weather for a location fronm the commandline

import json
import requests # Fetching Data over HTTPS
import sys

# Compute location from command line arguments
# If there is only one commandline argument, provide usage lines
if len(sys.argv) < 2:
    print('Usage: wu_weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1: ])

# TODO: Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?' + \
        'q={}&appid=ed613986d76fecf30a2a48f71f8de026'.format(location)
# Assign object to *response* and Confirm data is downloaded ok       
response = requests.get(url)
response.raise_for_status()

# TODO: LOAD JSON data into python variable
weather_data = json.loads(response.text)

#Print weather descriptions.

w = weather_data['list']
print('Current weather in {}:'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])