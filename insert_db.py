import sqlite3 as sql


con = sql.connect("my_first_database.db")
cur = con.cursor()

# name = input("Name: ")
# price = int(input("Price: "))

cur.execute("INSERT INTO students (name, age, coin) VALUES (?, ?, ?)", ("Kamoliddin", 15, 190))
con.commit()

# con.execute("INSERT INTO books (name, price) VALUES (?, ?)", (name, f"${price}"))
# con.commit()

name = input("Name: ")
country = input("Country: ")
color = input("Color: ")

cur.execute("INSERT INTO flowers (name, country, color) VALUES (?, ?, ?)", (name, country, color))
con.commit()


con.close()