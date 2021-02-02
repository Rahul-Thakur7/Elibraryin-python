from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()

class Storebook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Add book")
        self.resizable(FALSE, FALSE)

        self.top_frame = Frame(self, height=150, bg='gray')
        self.top_frame.pack(fill=X)

        heading = Label(self.top_frame, text="Add Book",
                        font='arial', bg='gray',fg='white')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self, height=650, bg='white')
        self.bodyframe.pack(fill=X)
        self.lablename = Label(
            self.bodyframe, text="Book Name", font='arial', bg='white')
        self.lablename.place(x=40, y=40)

        self.txt_book_name = Entry(self.bodyframe, width=30, bd=2)
        self.txt_book_name.place(x=200, y=45)

        self.lablename = Label(
            self.bodyframe, text="Author Name", font='arial', bg='white')
        self.lablename.place(x=40, y=80)

        self.txt_book_author = Entry(self.bodyframe, width=30, bd=2)
        self.txt_book_author.place(x=200, y=80)

        self.lablename = Label(
            self.bodyframe, text="Enter pages", font='arial', bg='white')
        self.lablename.place(x=40, y=120)

        self.txt_book_pages = Entry(self.bodyframe, width=30, bd=2)
        self.txt_book_pages.place(x=200, y=120)
        


        savebutton = Button(self.bodyframe, text="Save", command=self.savebook)
        savebutton.place(x=270, y=200)
    def savebook(self):
        bookname = self.txt_book_name.get()
        author = self.txt_book_author.get()
        pages = self.txt_book_pages.get()
     

        if(bookname and author and pages!= ""):
            try:
                query = "INSERT INTO 'books'(book_name, book_author, book_pages)VALUES(?,?,?)"
                cur.execute(query,(bookname, author,pages))
                con.commit()
                messagebox.showinfo(
                    "Success", "Book save successfully", icon='info')

            except:
                messagebox.showerror(
                    "Error", icon='warning'
                )
        else:

            messagebox.showerror(
                "Error", "All fields are mandatory", icon='warning'
            )

   
