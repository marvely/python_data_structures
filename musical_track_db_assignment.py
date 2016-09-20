import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect("musical_track_db.sqlite")
cur = conn.cursor()


# create tables
cur.execute('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
)''')

fname = raw_input("Enter file name: ")
if (len(fname) < 1): fname = "Library.xml"

#
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text #<---------- what is this? the text between tags.
        if child.tag == "key" and child.text == key: #<---- the entry we want.
            found = True
    return None
#<EOF>

stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict") # the data we want is in the third level dictionary
print "dict count:", len(all) # get an array of objects of how many dictionaries there

for entry in all:
    if ( lookup(entry, "Track ID") is None): continue

    name = lookup(entry, "Name")
    artist = look(entry, "Artist")
    album = lookup(entry, "Album") # album name
    genre = lookup(entry, "Genre")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    if name is None or artist is None or title is None: # sanity tracking
        continue
    print name, artist, album, genre, count, rating, length # now we have data

    cur.execute('''
    INSERT OR IGNORE INTO Artist (name)
    VALUES (?)''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, )) #<---- logical key is in the where clause
    artist_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Genre (name)
    VALUES (?)''', (genre, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (genre, )) #<---- logical key is in the where clause
    genre_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Album (title, artist_id) #<----- artist_id is the foriegn key
    VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) #<------ condense the code, replace is actually doing select, check and update in one line.
    VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))

conn.commit()

cur.close()
