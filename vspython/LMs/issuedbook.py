from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()



class IssuedBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Issued Book")
        self.resizable(FALSE, FALSE)

        self.top_frame = Frame(self, height=150, bg='gray')
        self.top_frame.pack(fill=X)

        heading = Label(self.top_frame, text="Issued Book",
                        font='arial', bg='gray',fg='white')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self, height=650, bg='white')
        self.bodyframe.pack(fill=X)
        '''books = cur.execute("SELECT * FROM books WHERE book_status=0").fetchall()
        booK_list = []
        for book in books:
            booK_list.append(str(book[0])+"-"+book[1])'''
            
        self.lbl_name = Label(
            self.bodyframe, text="Select Book", font='arial', bg='white')
        self.lbl_name.place(x=40, y=40)
                
        self.book_name =StringVar()
        self.book_combo = ttk.Combobox(
            self.bodyframe, textvariable=self.book_name)
        #self.book_combo['values'] = booK_list
    
        self.book_combo.place(x=200, y=45)
    
     

        self.lbl_author = Label(
            self.bodyframe, text="Select Member:", font='arial', bg='white')
        self.lbl_author.place(x=40, y=80)
        '''members = cur.execute("SELECT * FROM members WHERE book_status=0").fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0])+"-"+member[1])'''
            
        
        self.member_name =StringVar()
        self.member_combo = ttk.Combobox(
            self.bodyframe, textvariable=self.member_name)
        #self.member_combo['values'] = member_list
        self.member_combo.place(x=200, y=80) 
        
    
        savebutton = Button(self.bodyframe, text="Issue Now", command=self.issue_book)
        savebutton.place(x=270, y=200)

    def issue_book(self):
        selected_book = self.book_combo.get().split("-")[0]
        selected_member = self.member_combo.get().split("-")[0]
        try:
                query = "INSERT INTO issued_book(book_id,member_id)VALUES(?,?)"
                cur.execute(query,(selected_book,))
                con.commit()
                cur.execute(
                    "   UPDATE books SET book_status =1 WHERE book_id=?",(selected_book,selected_member)
                )
                con.commit()
                messagebox.showinfo(
                    "Success", "Bookissue successfully", icon='info')

        except:
            messagebox.showerror( "Error", icon='warning')
        
