import mysql.connector 

mydb = mysql.connector.connect(host='localhost', user='root', passwd="", database="mathenge")
mycursor= mydb.cursor()
# mycursor.execute('show databases')
# for i in mycursor:
#       print(i)
# creating table
# mycursor.execute("create table students(name varchar(255), regno varchar(100), county varchar(30), password int(30))")

# mycursor.execute('alter table students add column id int auto_increment primary key')
# mycursor.execute("create table students (name varchar(255), regno varchar(235), county varchar(30), password int(10))")
mycursor.execute("show tables")

for x in mycursor:
      print(x)



