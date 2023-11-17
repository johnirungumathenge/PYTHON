import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mathenge")

mycursor = mydb.cursor()
sql ="insert into student(Name, Email,Phone) values('john', 'jo@gmail.com', 938383)"
mycursor.execute(sql)
mydb.commit()

# result = mycursor.fetchall()
# for x in result:
#       print(x)