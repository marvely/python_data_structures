import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

# make tables
cur.execute('''
CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, #<------- python takes care of creating primary key for us!
    name TEXT UNIQUE
)''')
# don't want two same names in the table.

cur.execute('''
CREATE TABLE IF NOT EXISTS Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
)''')

fname = raw_input("Enter file name: ")
if (len(fname) < 1): fname = "Library.xml"

# the format of dictionary in the xml file:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# use lookup function to parse the dictionary file:
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text #<---------- what is this? the text between tags.
        if child.tag == "key" and child.text == key: #<---- the entry we want.
            found = True
    return None
# if found the tag, it will go to the next tag and return the value


stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict") # the data we want is in the third level dictionary
print "dict count:", len(all) # get an array of objects of how many dictionaries there

for entry in all:
    if ( lookup(entry, "Track ID") is None): continue

    name = lookup(entry, "Name")
    artist = look(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    if name is None or artist is None or Album is None: # sanity tracking
        continue
    print name, artist, album, count, rating, length # now we have data

    cur.execute('''
    INSERT OR IGNORE INTO Artist (name)
    VALUES (?)''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, )) #<---- logical key is in the where clause
    artist_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Album (title, artist_id) #<----- artist_id is the foriegn key
    VALUES (?, ?)''', (title, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) #<------ condense the code, replace is actually doing select, check and update in one line.
    VALUES (?, ?, ?, ?, ?)''', (name, album_id, length, rating, count)) #<------- 5 tuples

conn.commit()
