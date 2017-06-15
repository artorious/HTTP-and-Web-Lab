#!/usr/bin/env python
# wu_weather.py - Prints the weather for a location fronm the commandline

import json
import requests
import sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: wu_weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1: ])

# TODO: Download the JSON data from OpenWeatherMap.org's API

# TODO: LOAD JSON data into python variable

