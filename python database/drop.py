import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="",database="mathenge")

mycursor  = mydb.cursor()

# sql = "drop table students if exist"

# mycursor.execute(sql)

# mycursor.execute("create table customers (name varchar(233), address varchar(235))")
mycursor.execute("show tables")

for x in mycursor:
      print(x)
