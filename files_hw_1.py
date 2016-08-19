fname = raw_input("Enter file name: ")
# more elegant way to handle:
try:
  file_handle = open(fname)
except:
  print "Invalid filename"
  exit()
  
# function body:
for line in file_handle:
  line = line.rstrip() #remove new lines between each line
  print line.upper() #change all to uppercase
  
file_handle.close()
