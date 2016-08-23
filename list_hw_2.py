'''
Open the file mbox-short.txt and read it line by line. When you find a line that 
starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
'''

fname = raw_input("Enter file name: ")
try:
  fh = open(fname)
except:
  if len(fname) < 1 : 
    print "Invalid file name!"
    fname = raw_input("Enter file name: ")

count = 0
email_list = list()

for line in fh:
  if not line.startswith("From"):
    continue
  if line.startswith("From:"): 
    continue
  email = line.split()[1]
  #if not email in email_list:
  email_list.append(email)
  count += 1
# here they are not looking for the unique emails... allows duplicates!

for element in email_list:
  print element

print "There were", count, "lines in the file with From as the first word"
