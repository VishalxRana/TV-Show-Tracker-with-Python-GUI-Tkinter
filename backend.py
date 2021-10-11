import sqlite3


def connect():
    conn = sqlite3.connect("TV Shows Tracker with Tkinter/TvShows.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS TvShow (
        id INTEGER PRIMARY KEY,
        name text, 
        note text
        )""")
    conn.commit()
    conn.close()


def insert(name, note):
    conn = sqlite3.connect("TV Shows Tracker with Tkinter/TvShows.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO TvShow VALUES (NULL, ?, ?)", (name, note))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("TV Shows Tracker with Tkinter/TvShows.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TvShow")
    rows = cur.fetchall()
    conn.close()
    return rows 


def search(name='', note=''):
    conn = sqlite3.connect("TV Shows Tracker with Tkinter/TvShows.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TvShow where name=? OR note=?", (name, note))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("TV Shows Tracker with Tkinter/TvShows.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM TvShow WHERE id=?", (id,))
    conn.commit()
    conn.close() 


def edit(id, name='', note=''):
    conn = sqlite3.connect("TV Shows Tracker with Tkinter/TvShows.db")
    cur = conn.cursor()
    cur.execute("UPDATE TvShow SET name=?, note=? WHERE id=?", (name, note, id))
    conn.commit()
    conn.close() 


connect()
# insert("Peaky Blinders", "Completed mate!")
print(view())
# delete()

# Should be able to search with only 'breaking' or 'bad'
# Be able to search if entry is done in lower case. 
# lower() upper() and shayad proper() which make 1st letter of word upper and rest lower
# print(search(name="Suits"))