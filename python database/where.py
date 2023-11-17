import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="",database="mathenge")

mycursor = mydb.cursor()
# sql ="select * from students where county like '%Nak%'"
sql ="SELECT * FROM students WHERE name = '%s'"
adr = ("john")

mycursor.execute(sql, adr)

result = mycursor.fetchall()

for x in result:
      print(x)
