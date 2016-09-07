import urllib
import re
from bs4 import BeautifulSoup
url = raw_input('Enter -')
'''
Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_309541.html (Sum ends with 77)
'''

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

tag_list = list()
for tag in tags:
    '''
    print type(tag) #<---- this is a special type , bs4.element.tag... so cannot use findall
    print tag.get('class')
    print tag.Attrs
    '''
    tag_list.append(str(tag))

#print tag_list

num_list = list()
for element in tag_list:
    num = re.findall('[0-9]+', element)
    num_list.extend(num)

sum_of_num = sum(int(every_number) for every_number in num_list)
print sum_of_num
