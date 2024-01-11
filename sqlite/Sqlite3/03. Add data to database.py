import sqlite3

#Create the database file, here name is MyDataBase.db
conn = sqlite3.connect("MyDataBase.db") #extension can be anything. i.e .db, .sqlite3, .dbase, .ibrahim etc, preferrably .db
cur = conn.cursor()

print("Database Opened")

#Create a table named employee_records. The table will consist of:
# ID (int), NAME (text), DIVISION (text) and STARS (int) column
#NB: You can create multiple tables in a database
#PRIMATY KEY means unique data i.e 1,2,3... NO REPEATATION and there cannot be more than one primary key
#NOT NULL means the field should not remain empty.
#Can't create same table more than ones, hence error, hence the statement: IF NOT EXISTS
cur.execute (""" CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL 
)
""")

#Test text
print("Table Created")

#Add data to database 
cur.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
    VALUES(1,"Ibrahim","Software",7)
""")
# Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
# or specify the particular fields to insert into if not all
# But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS

#Apply changes to db using commit
conn.commit();
print("Changes applied")



#Close database when you are done with the dbase file
cur.close()
print("Database Closed")
