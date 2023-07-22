import sqlite3 as sql


con = sql.connect("my_first_database.db")
cur = con.cursor()


name = input("Name: ")
age = int(input("Age: "))
coin = int(input("Coin: "))

# cur.execute("DELETE FROM students)
# cur.execute("DELETE FROM students WHERE name = ?", ("Izzatilla",))
cur.execute("INSERT INTO students (name, age, coin) VALUES (?, ?, ?)", (name, age, coin))
con.commit()


Name = input("Name: ")

cur.execute("DELETE FROM students WHERE name = ?", (str(Name),))
con.commit()

con.close()