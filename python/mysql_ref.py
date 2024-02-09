import mysql.connector


'''
    === MYSQL PRIVILEGE ====
    Run this script in mysql to grant database access privilege
    NB (payslip is the name of the database we are trying to access)
    
GRANT ALL PRIVILEGES ON payslip.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'root'@'localhost'

-- NB: If error, replace all 'root' with 'admin' 

'''



def connect_to_mysql(host, username, password, database):
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        # Connection established successfully
        print("Connected to MySQL database successfully!")
        return conn
    except mysql.connector.Error as error:
        # Connection failed
        print("Failed to connect to MySQL database:", error)
        return False


# MySQL Connection Parameters
host = 'localhost'
username = 'root'
password = 'Admin123'
database = 'payslip'        # Name of database

# Attempt to connect to MySQL
connected = connect_to_mysql(host, username, password, database)

# Display the result
if connected:
    print("Connection successful!")
else:
    print("Connection failed!")
