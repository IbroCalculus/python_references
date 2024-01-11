import sqlite3

conn = sqlite3.connect("SQLite3.db")
cur = conn.cursor()
print('Database file opened')

cur.execute(""" CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL
)
""")

cur.execute(""" CREATE TABLE IF NOT EXISTS admin_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL
)
""")


def insert_record(ID, NAME, DIVISION, STARS):
    cur.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
        VALUES(?,?,?,?)""", (ID, NAME, DIVISION, STARS))
    # Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
    # or specify the particular fields to insert into if not all
    # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS

    # Apply changes to db using commit
    conn.commit()
    print("Changes applied")


def insert_recordADMIN(ID, NAME, DIVISION, STARS):
    query = f'INSERT INTO admin_records(ID,NAME,DIVSION, START) VALUES(?,?,?,?), ({ID}, {NAME}, {DIVISION}, {STARS})'
    cur.execute(query)
    # cur.execute(""" INSERT INTO admin_records(ID,NAME,DIVISION,STARS)
    #     VALUES(?,?,?,?)""", (ID, NAME, DIVISION, STARS))
    # Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
    # or specify the particular fields to insert into if not all
    # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS

    # Apply changes to db using commit
    conn.commit()
    print("Changes applied")


def read_records():
    # datas = cur.execute(""" SELECT ID, NAME, DIVISION, STARS FROM admin_records() """)
    # records = cur.execute(""" SELECT * FROM employee_records ORDER BY NAME DESC """)

    query = f' SELECT * FROM employee_records ORDER BY DIVISION ASC '
    records = cur.execute(query)

    for record in records:
        print(F'ID: {record[0]}; NAME: {record[1]}; DIVISION: {record[2]}; STARS: {record[3]}')


read_records()

def update_records(id1, id):
    query = f' UPDATE employee_records set ID={id1} WHERE ID={id}'
    cur.execute(query)
    conn.commit()

def delete_records(id):
    query = f' DELETE from employee_records WHERE ID={id} '
    cur.execute(query)
    conn.commit()
delete_records(4)

print('==============================')
read_records()

cur.close()
