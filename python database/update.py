import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="mathenge")

mycursor = mydb.cursor()

sql="update student set Name ='Kisumu' where Email='john@gmail.com'"

mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, 'rows affected')