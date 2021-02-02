from tkinter import *

from tkinter import messagebox
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()



class Storemember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Add Member")
        self.resizable(FALSE, FALSE)

        self.top_frame = Frame(self, height=150, bg='gray')
        self.top_frame.pack(fill=X)

        heading = Label(self.top_frame, text="Add Member",
                        font='arial', bg='gray',fg='white')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self, height=650, bg='white')
        self.bodyframe.pack(fill=X)

        self.lbl_name = Label(
            self.bodyframe, text="Enter Member Name", font='arial 12 bold', bg='white',fg='black')
        self.lbl_name.place(x=40, y=40)
        self.txt_member_name = Entry(self.bodyframe, width=30, bd=2)
        self.txt_member_name.place(x=200, y=45)

        self.lbl_author = Label(
            self.bodyframe, text="Enter Phone", font='arial', bg='white')
        self.lbl_author.place(x=40, y=80)

        self.txt_phone = Entry(self.bodyframe, width=30, bd=2)
        self.txt_phone.place(x=200, y=80)

        savebutton = Button(self.bodyframe, text="Save", command=self.savemember)
        savebutton.place(x=270, y=200)


    def savemember(self):
        name =  self.txt_member_name.get()
        phone = self.txt_phone.get()
       

        if(name and phone != ""):
            try:
                query = "INSERT INTO 'members'(member_name,member_phone)VALUES(?,?)"
                cur.execute(query,(name, phone))
                con.commit()
                messagebox.showinfo(
                    "Success", "Member save successfully", icon='info')

            except:
                messagebox.showerror(
                    "Error", icon='warning'
                )
        else:

            messagebox.showerror(
                "Error", "All fields are mandatory", icon='warning'
            )

    