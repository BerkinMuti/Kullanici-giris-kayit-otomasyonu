from tkinter import *
from tkinter import messagebox
def Register():
    import sqlite3
    vt = sqlite3.connect(r"C:\Users\Berkin Muti\Desktop\Python\kurs\Projelerim\User login-register automation\User login.db")
    cur = vt.cursor()
    cur.execute("Create table if not exists members(user_name varchar(20),Email varchar(50),password varchar(20))")
    name = txt_username.get()
    mail = txt_email.get()
    psw = txt_pass.get()
    try:
        cur.execute("Insert into members values (?,?,?)",(name,mail,psw))
        vt.commit()
        messagebox.showinfo("Information", "Register successful")
        canvas.destroy()
        import login
        login.canvas.mainloop()
        vt.close()
    except:
        messagebox.showwarning("Warning","Register failed")
        canvas.destroy()
canvas=Tk()
canvas.title("Register")
canvas.geometry("400x400")

Label(canvas,text="Username:",font=("Time News Roman",14)).place(x=5,y=35)

Label(canvas,text="E-Mail:",font=("Time News Roman",14)).place(x=5,y=75)

Label(canvas,text="Password:",font=("Time News Roman",14)).place(x=5,y=115)

txt_username=Entry(canvas,text="",font=("Time News Roman",14))
txt_username.place(x=130,y=35)

txt_email=Entry(canvas,text="",font=("Time News Roman",14))
txt_email.place(x=130,y=75)

txt_pass=Entry(canvas,show="*",text="",font=("Time News Roman",14))
txt_pass.place(x=130,y=115)

btn_register=Button(canvas,text="SAVE",width=16,bg="light blue",font=("Time News Roman",14),command=Register).place(x=130,y=150)

canvas.mainloop()