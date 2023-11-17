import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mathenge")

mycursor = mydb.cursor()

sql =" delete from students where county ='%s'"
nm = ("Nakuru")
mycursor.execute(sql, nm)
mydb.commit()

print(mycursor.rowcount, 'records deleted')