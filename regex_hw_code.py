import re

file_name = raw_input("Enter file:")
fh = open(file_name)

num_list = list()

for line in fh:
    line = line.rstrip()
    nums = re.findall(' *[0-9]+ *', line) #<---- some of the nums at the starting of the line, some of them at the end of the line...
    num_list.extend(nums)

sum_of_num = sum(int(every_number) for every_number in num_list)

print sum_of_num
fh.close()

'''
2 line version of this hw:
import re
print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
print sum( [******* **** * in re.findall('[0-9]+',  ]) )

AAARRRRRrrrrrr too hard to write in only 2 lines!!!!!!
'''
