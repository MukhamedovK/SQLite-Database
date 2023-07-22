import sqlite3 as sql


con = sql.connect("my_first_database.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
            name TEXT,
            age INTEGER,
            coin INTEGER
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS books(
            name TEXT,
            price INTEGER
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS flowers(
            name TEXT,
            country TEXT,
            color TEXT
            )""")

con.close()



