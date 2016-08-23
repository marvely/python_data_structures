'''
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = raw_input("Enter file: ")
try:
  file_handle = open(name)
except:
  print "Invalid file name!"
  exit()

email_list = list()

for line in file_handle:
  if not line.startswith("From"):
    continue
  if line.startswith("From:"): 
    continue 
  else:
    list_emails = line.split()[1]
    email_list.append(list_emails)

email_counts_dict = dict()
for name in email_list:
    email_counts_dict[name] = email_counts_dict.get(name, 0) + 1

# condense 4 lines code into 1 line!

#either create a new entry, or adds 1 to the current entry count!

# find the top counts, dict is very powerful and useful!

print "Dictionary contect print out line by line"
# can also print out the dict using a for-loop~
for key in email_counts_dict:
  print key, email_counts_dict[key]

# tuples 
print email_counts_dict.items()
for key, value in email_counts_dict.items():
  print key, value
  
# count the most common word in file
bigcount = None
bigemail = None
for email, count in email_counts_dict.items():
  if bigcount is None or count > bigcount:
    bigemail = email
    bigcount = count

print bigemail, bigcount #<----- this is the final outcome the hw is looking for.










file_handle.close()