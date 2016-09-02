import xml.etree.ElementTree as ET
input = '''<stuff>
  <users>
    <user x = "2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x = "7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input) # go down to the tree and grab all the things
lst = stuff.findall("users/user") # return a list of one entry of each user
print "User count:", len(lst) # count the users in the list
'''
the element in the list are XML node objects, that we can use other functions on
'''

for item in lst:
    print "Name", item.find("name").text
    print "Id", item.find("id").text # id gets the tag, and text gets the thing inside.
    print "Attribute", item.get("x")
