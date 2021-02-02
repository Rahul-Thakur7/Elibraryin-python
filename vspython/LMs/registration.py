from tkinter import *
import sqlite3
root=Tk()
root.title("Home page")
root.geometry("300x150")
root.configure(bg='sky blue')


#################################################        login         ###################################################################
def login():
	def login_database():
		conn=sqlite3.connect("Rahul.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
		row=cur.fetchall()
		conn.close()
		print(row)
		if row!=[]:
			user_name=row[0][1]
			L3.config(text="user name found with name: "+user_name)
		else:
			L3.config(text="user not found ")


                  
	root.destroy()
	login_root=Tk()
	login_root.title("Login page")
	login_root.geometry("500x250")
	login_root.configure(bg='sky blue')

	L1=Label(login_root,text="email",font="times 20",bg='sky blue')
	L1.grid(row=1,column=1)
	L2=Label(login_root,text="password",font="times 20",bg='sky blue')
	L2.grid(row=2,column=1)
	L3=Label(login_root,font="times 20",bg='sky blue')
	L3.grid(row=5,column=2)

	email_text=StringVar()
	e1=Entry(login_root,textvariable=email_text)
	e1.grid(row=1,column=2)
	password_text=StringVar()
	e2=Entry(login_root, show="*",textvariable=password_text)
	e2.grid(row=2,column=2)


	b1=Button(login_root,text="login",width=20,command=login_database)
	b1.grid(row=4,column=2)
	login_root.mainloop()
########################################                         signup                 ####################################################################################3

def signup():


	def signup_database():
		conn=sqlite3.connect("Rahul.db")
		cur=conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
		cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
		l4=Label(signup_root,text="account created",font="times 15")
		l4.grid(row=6,column=2)
		conn.commit()
		conn.close()





	root.destroy()
	signup_root=Tk()
	signup_root.title("Signup page")
	signup_root.configure(bg='sky blue')
	signup_root.geometry("500x250")
	L1=Label(signup_root,text="user name",font="times 20",bg='sky blue')
	L1.grid(row=1,column=1)
	L2=Label(signup_root,text="user email",font="times 20",bg='sky blue')
	L2.grid(row=2,column=1)
	L3=Label(signup_root,text="user password",font="times 20",bg='sky blue')
	L3.grid(row=3,column=1)


	name_text=StringVar()
	e1=Entry(signup_root,textvariable=name_text)
	e1.grid(row=1,column=2)
	email_text=StringVar()
	e2=Entry(signup_root,textvariable=email_text)
	e2.grid(row=2,column=2)
	password_text=StringVar()
	e3=Entry(signup_root, show="*",textvariable=password_text)
	e3.grid(row=3,column=2)

	b1=Button(signup_root,text="login",width=20,command=signup_database)
	b1.grid(row=4,column=2)
L1=Label(root,text="REGISTRATION FORM",font="times 20",bg='sky blue')
L1.grid(row=1,column=2,columnspan=2)
b1=Button(root,text="login",width=20,command=login)
b1.grid(row=2,column=2)

b2=Button(root,text="signup",width=20,command=signup)
b2.grid(row=2,column=3)
root.mainloop()

         
   
