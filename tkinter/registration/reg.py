from tkinter import *
import mysql.connector
from tkinter import messagebox
from subprocess import call


def Reg():
    mydb = mysql.connector.connect(host="localhost", user="root",password="", database="python")
    mycursor = mydb.cursor()
    
    name = name.get()
    uname = uname.get()
    email = email.get()
    password = password.get()
    cpassword = cpassword.get()
    
    
    if password == cpassword:
        sql ="insert into students(Username,Email,Password) values(%s,%s,%s)"
        val = (uname, email, password)
        result = mycursor.execute(sql, val)
        
        
        if result:
            messagebox.showinfo("registration successful")
            mydb.commit()
            return True
        
        else: 
            messagebox.showinfo("the query failed")
            
        
    else:
        messagebox.showinfo("password doesnt match")
        
    


root = Tk()
root.title("Registration form")
root.geometry("450x350")

title = Label(root, text="Register Here!", fg="red",font="georgia").grid(row=1, column=2, columnspan=5)
global e2

label1 = Label(root, text="Name").grid(row=2, column=1,padx=10, pady=10)
label5 = Label(root, text="Username").grid(row=3, column=1,padx=10, pady=10)
label2 = Label(root, text="Email").grid(row=4, column=1,padx=10, pady=10)
label3 = Label(root, text="Password").grid(row=5, column=1, padx=10, pady=10)
label4 = Label(root, text="C-password").grid(row=6, column=1, padx=10, pady=10)

e1 = Entry(root, width=25).grid(row=2,column=2)
e2 = Entry(root,width=25).grid(row=3,column=2)
e3 = Entry(root,width=25).grid(row=4,column=2)
e4 = Entry(root,width=25, show="*").grid(row=5,column=2)
e5 = Entry(root,width=25, show="*").grid(row=6,column=2)

def click():
    label = Label(root, text=e2.get).place(x=10, y=300)
    return True
    
btn = Button(root, text="register", width=10, bg="black", fg="white",command=click).grid(row=7, column=2)

root.mainloop()
