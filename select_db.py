import sqlite3 as sql


con = sql.connect("my_first_database.db")
cur = con.cursor()

# data = cur.execute("SELECT name FROM students").fetchall()
# data = cur.execute("SELECT * FROM students").fetchall()     # fetchall() = берет все элементы 
# one_data = cur.execute("SELECT * FROM students").fetchone()  # fetchone() = берет первый элементы
# many_data = cur.execute("SELECT * FROM students").fetchmany(size=2)  # fetchmany() = берет указанные элементы

# print(data)
# print(one_data)
# print(many_data)


# data = cur.execute("SELECT * FROM students WHERE age < 15").fetchall()
# data = cur.execute("SELECT * FROM students WHERE age = 15 OR age = 14 ORDER BY coin ASC").fetchall() # ORDER BY coin ASC - сортировка по coin возрастание
# data = cur.execute("SELECT * FROM students WHERE age = 15 OR age = 14 ORDER BY coin DESC").fetchall() # ORDER BY coin DESC - сортировка по coin убывание
# print(data)


# data = cur.execute("SELECT * FROM students WHERE coin >= 190 ORDER BY coin ASC").fetchall()
# data1 = cur.execute("SELECT name FROM students ORDER BY name DESC").fetchall()
# print(data)
# print(data1)

data = cur.execute("SELECT name, age FROM students ORDER BY coin ASC").fetchall()

context = ""
for item in data:
    context += f"Ism: {item[0]} || Yosh: {item[1]}\n"

print(context)



con.close()
