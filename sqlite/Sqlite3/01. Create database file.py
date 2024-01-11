import sqlite3

#Create the database file, here name is MyDataBase.db
conn = sqlite3.connect("MyDataBase.db") #extension can be anything. i.e .db, .sqlite3, .dbase, .ibrahim etc, preferrably .db
cur = conn.cursor()                     #Handle for working with the database

print("Database Opened")

#Close database when you are done with the dbase file
cur.close()

print("Database Closed")
