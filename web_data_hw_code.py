import re
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL -')
count = int(raw_input('Enter count -'))
position = int(raw_input('Enter position -'))

def get_tags_from_soup(input_url):
  print "starting with this:", input_url
  html = urllib.urlopen(input_url).read()
  soup = BeautifulSoup(html, 'lxml')
  tags = soup('a')
  tag_list = list()
  for tag in tags:
      tag_list.append(str(tag.get('href', None)))
  global url
  url = tag_list[position -1]
  return url
# lesson learnt: need to change the value in the global level!!!!!!!!!!!!
'''
Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Samarjit.html
'''
for i in range(0, count + 1):
    get_tags_from_soup(url)
