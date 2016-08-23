# a range input a variables will be a list of integers
x = range(5)
print x

# if you add 2 lists together, its appendix
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print len(c)

# how to slice a list?
t = [9, 41, 12, 3, 74, 15]
print t[2:4]

# assignment 1
'''
 Open the file romeo.txt and read it line by line. For each line, split the line into 
 a list of words using the split() method. The program should build a list of words. 
 For each word on each line check to see if the word is already in the list and if not 
 append it to the list. When the program completes, sort and print the resulting words 
in alphabetical order.
'''
fname = raw_input("Enter file name: ")
try:
  fh = open(fname)
except:
  print "Invalid Name!"
  exit()

# the function body:
file_list = list()
for line in fh:
  line = line.rstrip()
  split_words = line.split()
  for word in split_words:
    if not word in file_list:
      file_list.append(word)

print sorted(file_list)

fh.close()
