# Use the file name mbox-short.txt as the file name
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
  fh = open(fname)
except:
  print "Invalid file name!"
  exit()

count_line = 0
sc = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
      continue
    count_line += 1
    dig_pos = line.find(".")
    float_num = float(line[dig_pos-1:])
    sc = sc + float_num

print "Average spam confidence:", sc/count_line

fh.close()
