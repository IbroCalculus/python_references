import mysql.connector  # pip install mysql-connector

'''
    === MYSQL PRIVILEGE ====
    Run this script in mysql to grant database access privilege
    NB (sampledb is the name of the database we are trying to access)
    
GRANT ALL PRIVILEGES ON sampledb.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'root'@'localhost'

-- NB: If error, replace all 'root' with 'admin' 

'''


def connect_to_db(host, username, password, database):
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database  # This is optional when connecting to MySQL if perhaps want to programmatically create database. Better to add
        )
        print("Connected to database successfully!")
        return conn
    except mysql.connector.Error as error:
        print(f"Connection to database failed! Error occurred of type: {error}")
        return False


host = 'localhost'
username = 'root'
password = 'Admin123'
database = 'sampledb'

connected = connect_to_db(host, username, password, database)
if connected:
    mycursor = connected.cursor()


# ==================== 1. CREATE DATABASE ==================
def create_database():
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS sampledb2")
        mycursor.execute("USE sampledb2")
        print("Database selected successfully")
    except Exception as e:
        print(f"Database creation failed. Error occurred of type: {e}")



def create_table():
    try:
        query = "CREATE TABLE IF NOT EXISTS person(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, first_name VARCHAR(50) NOT NULL, surname VARCHAR(50) NOT NULL, age INT(20) NOT NULL)"
        mycursor.execute(query)
        print("Table created successfully")
    except Exception as e:
        print(f"Table creation failed. Error occurred of type: {e}")


def insert_to_table(first_name, surname, age):
    try:
        query = "INSERT INTO person (first_name, surname, age) VALUES (%s, %s, %s)"
        val = (first_name, surname, age)
        mycursor.execute(query, val)
        connected.commit()
        print("Data inserted successfully")
    except Exception as e:
        print(f"Failed to insert to db. Error occurred of type: {e}")

def retrieveAllFromDb():
    try:
        query = "SELECT * FROM person"
        mycursor.execute(query)
        for row in mycursor:
            # print(row)
            id = row[0]
            first_name = row[1]
            surname = row[2]
            age = row[3]
            print(f'ID: {id}, FIRST NAME: {first_name}, SURNAME: {surname}, AGE: {age}')
        print("Data retrieved successfully")
    except Exception as e:
        print(f"Error occurred of type: {e}")

def retrieveById(id):
    try:
        query = "SELECT * FROM person WHERE id = %s"
        val = (id,)
        mycursor.execute(query, val)
        for row in mycursor:
            # print(row)
            id = row[0]
            first_name = row[1]
            surname = row[2]
            age = row[3]
            print(f'ID: {id}, FIRST NAME: {first_name}, SURNAME: {surname}, AGE: {age}')
        print("Data retrieved successfully")
    except Exception as e:
        print(f"Error occurred of type: {e}")


def updateById(id, first_name, age):
    try:
        query = "UPDATE person SET first_name = %s, age = %s WHERE id = %s"
        val = (first_name, age, id)
        mycursor.execute(query, val)
        connected.commit()
        print("Data updated successfully")
    except Exception as e:
        print(f"Error occurred of type: {e}")

# ============================ USAGES =================

# create_database()
# create_table()
# insert_to_table("Jerremi", "Fisher", 21)
# retrieveAllFromDb()
# retrieveById(12)
# updateById(12, "Karamel", 67)
# retrieveById(12)