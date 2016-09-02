import urllib
import xml.etree.ElementTree as ET

'''
Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_309538.xml (Sum ends with 16)
'''

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data
    tree = ET.fromstring(data)

    comments = tree.findall('comments/comment')
    print "Count:", len(comments)

    sum = 0
    for element in comments:
        num = int(element.find("count").text)
        sum += num

    print sum
