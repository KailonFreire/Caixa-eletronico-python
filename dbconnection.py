import mysql.connector

# establish a connection to the database
mydb = mysql.connector.connect(
  host="localhost:3306",
  user="root",
  password="",
  database="caixaeletronico"
)

mycursor = mydb.cursor()

select = mycursor.execute("SELECT * FROM yourtable")
create = mycursor.execute("CREATE TABLE ")
insert = mycursor.execute("INSERT INTO ")

result = mycursor.fetchall()

for row in result:
  print(row)
