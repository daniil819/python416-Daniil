import sqlite3

car_list = [
    ('BMW', 54000),
    ('Chevrolet', 46000),
    ('Daewoo', 38000),
    ('Citroen', 29000),
    ('Honda', 33000)
]

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)

# cur.executescript("""
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO cars VALUES(NULL, ?,?)", car_list)

# for car in car_list:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?,?)", car)
# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)"),
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)"),
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)"),
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)"),
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit()  # сохраняет соединение в базу данных
# con.close()

# 2 добавление
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# добавление из таблицы
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_id = cur.lastrowid
#     buy_id = 2
#     cur.execute("INSERT INTO cost  VALUES('Илья', ?, ?)", (last_id, buy_id))

# Просмотр данных
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     con.row_factory = sqlite3.Row
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # print(rows)
#
#     rows2 = cur.fetchone()
#     print(rows2)
#
#     rows3 = cur.fetchmany(5)
#     print(rows3)
#
#     for res in cur:
#         print(res)


# добавление картинок
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );""")
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute('SELECT ava FROM users')
#     img = cur.fetchone()['ava']
#     write_ava('out.png', img)

# ПОлучение всех данных в виде кода
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open('sql_dump.sql', 'w') as f:
#         for sql in con.iterdump():
#             f.write(sql)

# Сохранение
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)

with sqlite3.connect("cars_db.db") as con:
    cur = con.cursor()

    with open("sql_dump.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)
