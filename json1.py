import json

data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}'''
print "part1"
info = json.loads(data) # json sees a {}, and it is a dictionary
print "Name:", info["name"]
print "Hide:", info["email"]["hide"] #native dictionary

'''
part2
'''
print "part2"
input = '''[
  {"id" : "001",
   "x" : "2",
   "name" : "Chuck"
  },
  {"id" : "009",
   "x" : "7",
   "name" : "Chuck"
   }
]'''

info2 = json.loads(input) # really a list.
print "User count:", len(info2)

for item in info2:
    print "Name", item["name"]
    print "Id", item["id"]
    print "Attribute", item["x"]
