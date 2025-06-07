import sqlite3

with sqlite3.connect("users.db") as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+7 909 1234554",
    # age INTEGER CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")

    # Переименование таблицы
    # cur.execute("""
    # ALTER TABLE users
    # RENAME TO person_table;
    # """)

    # добавление нового столбца
    # cur.execute("""
    #    ALTER TABLE person_table
    #    ADD COLUMN address TEXT;
    #    """)

    # перменование столбца
    cur.execute("""
       ALTER TABLE person_table
       ADD COLUMN address TO home_address;
       """)
