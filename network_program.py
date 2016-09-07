# nice thing there is a socket library in py?!
import socket
# this is the way to open a port-whole to the internet?
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # a string socket.
# find a connect to mysock
mysock.connect(('www.py4inf.com', #<--- host
                 80)) #<--- port
'''
sockets are like making a phone call, and the applications are what you see or hear over the phone calls.
'''
mysock.send('GET http://www.py4inf.com/code/remeo.txt HTTP/1.0\n\n')

# read the file, upto 512 characters long
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data
mysock.close()


# too bad.... the doc has been moved :(

'''
a more advanced way, and easier way to do?
'''
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/remeo.txt')
# but it only get the file(body), no header or anything.

for line in fhand:
    print line.strip()
'''
Beautiful soup!
'''
import urllib
from bs4 import BeautifulSoup
url = raw_input('Enter -')

html = urllib.urlopen(url).read() # all the lines in a single call with all the tags... a STRING of entire page text
soup = BeautifulSoup(html) #<--- call it to figure this out. It is a parsed html data.
#soup object.

# Retrieve a list of the anchor tags
# Each tag is like a dict of HTML attributes

tags = soup('a') #<a ... > </a> this is what anchor tags look like
# return a dict of tags, values pair.

for tag in tags:
    print 'TAG:', tag
    print 'URL:', tag.get('href', None) # <----- do it like a dict!
    print 'Contents:', tag.Contents[0]
    print 'Attrs:', tag.Attrs
