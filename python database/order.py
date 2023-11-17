import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mathenge")

mycursor = mydb.cursor()

sql = "select * from students order by name desc"

mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
      print(x)