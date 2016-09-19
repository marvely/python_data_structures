import sqlite3

conm = sqlite3.connect("emaildb.sqlite")
cur = conm.cursor()

# cursor object?
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input("Enter file name:")
if (len(fname) < 1): fname = "mbox-short.txt"
file_handler = open(fname)

for line in file_handler:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute("SELECT count FROM Counts WHERE email = ?", (email, ))
# the first thing in the tuples is going to be substitute in the ?
    try:
        count = cur.fetchone()[0] # bring back one row into memory and make it a list
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email, ))
    except:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email, ))

    conm.commit() #everything im done until now, write into disk

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"
# ust this "str" guy to pull stuff out from the database.

for row in cur.execute(sqlstr):
    print str(row[0], row[1])

cur.close()

# running a dictionary in the database
# so we can store a lot in the database and run one row at a time, save some memory!!!!
