#### regular expression
import re
hand = open("mbox-short.txt")

for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print line

for line in hand:
    line = line.rstrip()
    if re.search("^From:", line): #<------ a line start with from!
        print line
'''
when using re.findall(), the result will be a list
when re.search(), it will return true or false result
these functions are gready??...
Non gready matching, ?
'''
x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('^From (\S+@\S+)', x ) # make a reallt long regex, but only pull out the important one
print y

'''
looking for the domain name?
do this using the regex~~
'''
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y =  re.findall('@([^ ]*)', lin)
y1 = re.findall('^From .*@([^ ]*)', lin) #<---- very condensed code!
print y
print y1
'''
re-write the spam code
'''
import re
fh = open('mbox-short.txt')
numlist = list()

for line in fh:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence:  ([0-9.]+)', line) # the . is actual period inside the brackets.
    if len(stuff) !=1: continue #here I only looking for exact 1 match.
    num = float(stuff[0])
    numlist.append(num)
# the regex code is both selecting and extracting at the same time! Efficient!

print 'Maximum:', max(numlist)
'''
Escape Character
'''
import re
x = 'We just received $10.00 for cookies.'
y3 = re.findall('\$[0-9.]+', x) # the backslash makes the dollar sign a real dollar sign.
print y3
