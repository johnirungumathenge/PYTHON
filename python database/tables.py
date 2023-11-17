import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mathenge")

mycursor = mydb.cursor()

sql = "insert into students (name, regno, county, password) values(%s, %s, %s, %s)"

val = [("Delo", "CT203/103351/20", 'Nakuru','1239'),
       ("Paul", "CT203/103352/20", 'Muranga','1252'),
       ("Njenga", "CT203/103353/20", 'Nyandarua','8734'),
       ("Kim", "CT203/103354/20", 'Nanyuki','1285'),
       ("Chege", "CT203/103355/20", 'Bomet','1276'),
       ("kamau", "CT203/103356/20", 'Nyeri','4755'),
       ("James", "CT203/103357/20", 'Isiolo','393'),
       ("Titus", "CT203/103358/20", 'Meru','3684'),
       ("Trizza", "CT203/103359/20", 'Nanyuki','0328'),
       ("lucy", "CT203/103360/20", 'Laikipia','6785'),
       ("ann", "CT203/103361/20", 'Molo','0294'),
       ("Jane", "CT203/103362/20", 'Nairobi','3939'),
       ("Mirriam", "CT203/103363/20", 'Machakos','0933'),
       ("Monicah", "CT203/103364/20", 'Kisumu','1256'),
       ("Simo", "CT203/103365/20", 'Nakuru','1209')      
       
       ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, 'the rows added')
print(mycursor.lastrowid)