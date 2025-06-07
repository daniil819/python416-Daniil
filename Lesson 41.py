import sqlite3

with sqlite3.connect("db_3.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT * 
    FROM T1
    LIMIT 2, 5
    """)
    # for res in cur:
    #     print(res)

    # res = cur.fetchall()
    # print(res)

    # res1 = cur.fetchone()
    # print(res1)

    res2 = cur.fetchmany(2)
    print(res2)

    res1 = cur.fetchone()
    print(res1)