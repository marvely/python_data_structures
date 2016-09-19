'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_309542.json (Sum ends with 35)
'''
import urllib
import json

while True:
    url = raw_input("Enter address: ")
    if len(url) < 1: break # if no input, then exit the program.

    print "Retrieving,", url

    url_handle = urllib.urlopen(url)
    data_in_url = url_handle.read()

    print "Retrieved,", len(data_in_url), "characters"

    try: js_data = json.loads(data_in_url)
    except: js_data = None

    #print json.dumps(js_data, indent = 4)

    count_of_comments = 0
    sum_of_counts = 0
    for names in js_data['comments']:
        count = names['count']
        sum_of_counts += count
        count_of_comments += 1
    print "Count:", count_of_comments
    print "Sum:", sum_of_counts
