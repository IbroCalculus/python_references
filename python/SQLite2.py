import sqlite3

#NB: For every cur.execute(), you can use a query string to make it easier. E.G:
# query = f' SELECT ID, NAME, DIVISION, STARS FROM employee_records '
# datas = cur.execute(query)

#1. CREATE or OPEN A DATABASE FILE
'''
    conn = sqlite3.connect("MyDataBase.db") #extension can be anything. i.e .db, .sqlite3, .dbase, .ibrahim etc, preferrably .db
    cur = conn.cursor()                     #Handle for working with the database
    
    #Close database when you are done with the dbase file
    cur.close()
'''

#2. CREATE A TABLE
#NB: There cannot be more than 1 primary key in a table
'''
    cur.execute (""" CREATE TABLE IF NOT EXISTS employee_records(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        DIVISION TEXT NOT NULL,
        STARS INT NOT NULL
    )
    """)
'''

#3. ADD DATA TO DATABASE TABLE
'''
    cur.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
        VALUES(1,"Ibrahim","Software",5)
    """)
    # Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
    # or specify the particular fields to insert into if not all
    # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS
    
    #Apply changes to db using commit
    conn.commit()
'''

#4. #ADD DATA TO DATABASE USING A FUNCTION WITH PARAMETERS
'''
    def insert_record(ID,NAME,DIVISION,STARS):
        
        #USING QUERY STRING, BETTER WAY
        query = f'INSERT INTO admin_records(ID,NAME,DIVSION, START) VALUES(?,?,?,?), ({ID}, {NAME}, {DIVISION}, {STARS})'
        cur.execute(query)
        
        #cur.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS) VALUES(?,?,?,?)""",(ID,NAME,DIVISION,STARS))
        # Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
        # or specify the particular fields to insert into if not all
        # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS
    
        #Apply changes to db using commit
        conn.commit()
        print("Changes applied")
    
    insert_record(5,"Muhammad","Soldier",9)
    
    
    #Close database when you are done with the dbase file
    cur.close()
'''


#5. #READ DATA FROM DATABASE
'''
def read_records():
    # datas = cur.execute(""" SELECT ID, NAME, DIVISION, STARS FROM employee_records """)
    #records = cur.execute(""" SELECT * FROM employee_records """)
    #records = cur.execute(""" SELECT * FROM employee_records ORDER BY NAME """)
    #records = cur.execute(""" SELECT * FROM employee_records ORDER BY NAME DESC """)
    #records = cur.execute(""" SELECT * FROM employee_records ORDER BY NAME ASC """)
    
    #USING QUERY STRING, BETTER WAY
    query = f' SELECT * FROM employee_records ORDER BY NAME DESC '
    records = cur.execute(query)
    
    for record in records:
        print(f' ID: {record[0]}; NAME: {record[1]}; DIVISION: {record[2]}; STARS: {record[3]}')
'''



#6. #UPDATING A RECORD
'''
def update_records(name, id):
    query = f' UPDATE employee_records set NAME="{name}" WHERE ID={id}'  #the '{name}' implies it's a string value
    cur.execute(query)
    conn.commit()

update_records("Suleiman Ibrahim", 2)
'''


#7. #DELETE A RECORD
'''
def delete_records(id):
    query = f' DELETE from employee_records WHERE ID={id} '
    cur.execute(query)
    conn.commit()
'''


#8. #DELETE A TABLE
'''
 query = DROP TABLE admin_records
 query = DROP TABLE IF EXISTS admin_records
'''