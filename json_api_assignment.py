'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py.
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON.
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://python-data.dr-chuck.net/geojson

This API uses the same parameters (sensor and address) as the Google API.
This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API. To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py
'''
import urllib
import json

service_url = 'http://python-data.dr-chuck.net/geojson?'

while True:
    place_name = raw_input("Enter Place Name: ")
    if len(place_name) < 1: break
    url = service_url + urllib.urlencode({"sensor": "false", "address": place_name})
    print "Retrieving", url

    url_handle = urllib.urlopen(url)
    data_in_url = url_handle.read()
    print "Retrieved,", len(data_in_url), "characters"

    try: js_data = json.loads(str(data_in_url))
    except: js_data = None
    if "status" not in js_data or js_data["status"] != "OK":
        print "==== Failure To Retrieve ===="
        print js_data
        continue
    #print json.dumps(js_data, indent = 4) # pretty print json inside python :)

    place_id = js_data['results'][0]['place_id']
    print place_id
