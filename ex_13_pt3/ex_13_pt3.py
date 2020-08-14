# Calling a JSON API In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve
# JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a
# textual identifier that uniquely identifies a place as within Google Maps.
#
# API End Points
#
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#
# http://py4e-data.dr-chuck.net/json?
#
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as
# often as you like. If you visit the URL with no parameters, you get "No address..." response.
#
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the
# address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in
# http://www.py4e.com/code3/geojson.py
#
# Make sure to check that your code is using the API endpoint is as shown above. You will get different results from
# the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

# Escuela Superior Politecnica del Litoral

# Problem definition: print the place_id of an address or location.
# 1 - Enter the address;
# 2 - Get the place_id of the address;
# 3 - Print the place_id.

import json
import urllib.request
import urllib.parse

address = input("Enter Location:")
print("Retrieving", address)

service_url = "http://py4e-data.dr-chuck.net/json?"
query_string = urllib.parse.urlencode({"key":42, "address":address})
url = service_url + query_string

with urllib.request.urlopen(url) as response:
    response_body = response.read().decode()
    print("Retrieved", len(response_body), "characters")
    data = json.loads(response_body)
    for item in data["results"]:
        print("Place id", item["place_id"])







