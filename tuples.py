
# tuples are much more efficient!
# when you are create list that never changing, or one time thing (temporary lists)
# on the left hand side, they must be variables in the tuples!

# dict.items() will return a list of tuples (key, value)

# tuples are comparable~~~ and things can be compared can also be sorted~~~

'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
hour_list = list()
# create a list of hours data
fname = raw_input("Enter file name: ")
try:
  fh = open(fname)
except:
  if len(fname) < 1 : 
    print "Invalid file name!"
    fname = raw_input("Enter file name: ")

for line in fh:
  if not line.startswith("From"):
    continue
  if line.startswith("From:"): 
    continue
  time_before = line.split()[5]
  hour_splited = time_before.split(":")[0]
  hour_list.append(hour_splited)
#
# create a dict of hour, counts pair data
hour_counts_pair_dict = dict()
for hour in hour_list:
  hour_counts_pair_dict[hour] = hour_counts_pair_dict.get(hour, 0) + 1

for h, c in sorted(hour_counts_pair_dict.items()):
  print h, c

fh.close()