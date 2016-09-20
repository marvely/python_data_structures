import sqlite3
import re

#create a database in .sqlite format
conm = sqlite3.connect("email_domain_db.sqlite")
cur = conm.cursor()

# cursor object?
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input("Enter file name:")
if (len(fname) < 1): fname = "mbox-short.txt"
file_handler = open(fname)

for line in file_handler:
    if not line.startswith("From: "): continue
    org = re.findall("^From: \S+@(\S+)", line)[0]
    #print domain_name
    cur.execute("SELECT count FROM Counts WHERE org = ?", (org, ))

    try:
        count = cur.fetchone()[0]
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org, ))
    except:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org, ))

conm.commit()

sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
