import mysql.connector

def start():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='235711',
        auth_plugin='mysql_native_password'
    )

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS caixa_eletronico")

    with open('SQL/createTable.sql', 'r') as createTable:
        query = createTable.read()

    cursor.execute(query, multi=True)

    cursor.close()
    conn.close()

def createConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="caixa_eletronico"
    )
