#http://python-data.dr-chuck.net/known_by_Montgomery.html
import re
import urllib
from bs4 import BeautifulSoup
tag_list = list()
html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Montgomery.html').read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    tag_list.append(str(tag.get('href', None)))
print tag_list[2]
