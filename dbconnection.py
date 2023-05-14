import mysql.connector

def create_database():
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS caixa_eletronico")

    # Close the cursor and connection
    cursor.close()
    conn.close()

def connect():
    # Establish a connection to the MySQL server and database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        database="caixa_eletronico"
    )

    return conn


    
