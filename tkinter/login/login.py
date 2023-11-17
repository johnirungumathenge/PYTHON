from tkinter import *
import mysql.connector

from tkinter import messagebox
from subprocess import call


def ok():
    mydb = mysql.connector.connect(host="localhost", user="root",password="", database="login")
    mycursor = mydb.cursor()
    Uname = e1.get()
    Password = e2.get()
    
    sql = "select * from students where Uname = %s and Password = %s"
    mycursor.execute(sql, [(Uname), (Password)])
    result = mycursor.fetchall()
    if result:
        messagebox.showinfo("","login success")
        root.destroy()
        #call(["python","login.py"])
        return True
    
    else:
        messagebox.showinfo("","incorrect username and password")
        return False


def reg():
    mydb = mysql.connector.connect(host="localhost", user="root",password="", database="login")
    mycursor = mydb.cursor()
    
    username = e1.get()
    password = e2.get()
    
    sql = "insert into students(Uname,Password) values(%s,%s)"
    val = (username,password)
    result = mycursor.execute(sql, val)
    mydb.commit()
    
    if result:
        messagebox.showinfo("registration success")
        root.destroy()
        return True
        
    else:
        messagebox.showinfo("registration failed")
        return False
    
    
      
    
    
    
root = Tk()
root.title("login Form")
root.geometry("300x200")

global e1
global e2

usename = Label(root, text="username").place(x=10, y=20)
password = Label(root, text="Password").place(x=10, y=50)

e1 = Entry(root)
e1.place(x=100, y=20)

e2 = Entry(root)
e2.place(x=100, y=50)
e2.config(show='*')

btn = Button(root, text='login', height=3, width=10, command=ok).place(x=50, y=100)

brt2 = Button(root, text="register", height=3, width=10, command=reg).place(x=180,y=100)
root.mainloop()