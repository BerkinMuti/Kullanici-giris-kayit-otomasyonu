from tkinter import *
from tkinter import messagebox

def login():
    import sqlite3
    vt = sqlite3.connect(r"C:\Users\Berkin Muti\Desktop\Python\kurs\Projelerim\User login-register automation\User login.db")
    cur = vt.cursor()
    name=username.get()
    mail = e_mail.get()
    psw=password.get()
    cur.execute("Select * from members where user_name=? and email=? and password=?",(name,mail,psw))
    data=cur.fetchall()
    if len(data)==0:
        messagebox.showwarning("WARNING", "There is no such user")
    else:
        messagebox.showinfo("Welcome","Hello "+name)

def register():
    canvas.destroy()
    import register
    register.canvas.mainloop()

canvas=Tk()
canvas.geometry("400x400")
canvas.title("User Login")

Label(canvas,text="Username:",font=("Time News Roman",14)).place(x=5,y=30)
Label(canvas,text="E-Mail:",font=("Time News Roman",14)).place(x=5,y=60)
Label(canvas,text="Password:",font=("Time News Roman",14)).place(x=5,y=90)

username=Entry(canvas,width=20,font=("Time News Roman",14))
username.place(x=130,y=35)
e_mail=Entry(canvas,width=20,font=("Time News Roman",14))
e_mail.place(x=130,y=65)
password=Entry(canvas,show="*",width=20,font=("Time News Roman",14))
password.place(x=130,y=95)

buton1=Button(canvas,text="Login",width=16,bg="light blue",font=("Time News Roman",14),command=login)
buton1.place(x=130,y=130)
buton2=Button(canvas,text="Register",width=16,bg="light blue",font=("Time News Roman",14),command=register)
buton2.place(x=130,y=180)

canvas.mainloop()