from tkinter import *
from tkinter import ttk
import sqlite3
import importlib
bookwindow = importlib.import_module("Book")
memberwindow = importlib.import_module("newmember")
issuedbookwindow = importlib.import_module("issuedbook")

con = sqlite3.connect("Library.db")
cur = con.cursor()


class Main(object):
    def __init__(self, master):
        self.master = master
        def showbooks(self):
                
            books = cur.execute("SELECT * FROM books").fetchall()
       
            counter = 0
            for book in books:
                self.management_box.insert(counter,str(book[0])+"-"+book[1])
                counter += 1

        ##main frame


        mainFrame = Frame(self.master)
        mainFrame.pack()

        ###top frame
        topFrame = Frame(mainFrame, width=900, height=70,
                         borderwidth=2, relief=SUNKEN, padx=20)

        topFrame.pack(side=TOP, fill=X)

        ########################

        self.btn_add_member = Button(
            topFrame, text='New member', font="arial", padx=20)
        self.btn_add_member.configure(command = self.new_member)
        self.btn_add_member.pack(side=LEFT)

       
        self.btn_new_book = Button(
            topFrame, text='New Book', font="arial", padx=20, )
        self.btn_new_book.configure(command=self.Book)
        self.btn_new_book.pack(side=LEFT)
        
        self.btn_issue_book = Button(
            topFrame, text='Issue Book', font="arial", padx=20)
        self.btn_issue_book .configure(command = self.issued_book) 
        self.btn_issue_book.pack(side=LEFT)


        ##centre frame
        centerFrame = Frame(mainFrame, width=900, height=800, borderwidth=2, relief=RIDGE)
        centerFrame.pack(side=TOP)

        ##left frame
        leftFrame = Frame(centerFrame, width=600, height=700, borderwidth=2, relief=SUNKEN)
        leftFrame.pack(side=LEFT)

        self.lefttab = ttk.Notebook(leftFrame, width=600, height=700)
        self.lefttab.pack()
        self.tab1 = ttk.Frame(self.lefttab)
        self.tab2 = ttk.Frame(self.lefttab)
        self.lefttab.add(self.tab1, text="Management")
        self.lefttab.add(self.tab2, text="Summary")

        ##----------------Management----------------------------------------##
        self.management_box = Listbox(
            self.tab1, width=40, height=30, font='arial')
        self.Sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.management_box.grid(
            row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.Sb.config(command=self.management_box.yview)
        self.management_box.config(yscrollcommand=self.Sb.set) 
        self.Sb.grid(row=0, column=0, sticky=N + S + E)

        self.list_details = Listbox(self.tab1, width=40, height=30, font='arial')
        self.list_details.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)

        ##----------------Summary------------------------------------------##
        self.lbl_book_count = Label(self.tab2, text="Books", pady=20, font='verdana')
        self.lbl_book_count.grid(row=0)

        self.lb1_member_counter = Label(self.tab2, text="Members", pady=20, font='verdana')
        self.lb1_member_counter.grid(row=1, sticky=W)
        self.lb1_taken_count = Label(self.tab2, text="In Stock", pady=20, font='verdana')
        self.lb1_taken_count.grid(row=2, sticky=W)


        ##right frame
        rightFrame = Frame(centerFrame, width=300, height=700, borderwidth=2, relief=SUNKEN)
        rightFrame.pack()


        ########################
        searchbar = LabelFrame(rightFrame, width=250, height=70, font='arial', text="Search")
        searchbar.pack(fill=BOTH)
        self.lbl_search = Label(
            searchbar, text="Search Book:", font='arial'
        )
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        
        self.ent_search = Entry(searchbar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        
        self.btn_search_btn= Button(
            searchbar, text='Search now')
        self.btn_search_btn.grid(row=0, column=4, padx=20, pady=10)

        list_bar = LabelFrame(rightFrame, width=280,
                                         height=200, text="Book list", font='arial')
        list_bar.pack(fill=BOTH)

        list_lbl = Label(list_bar, text="Sort by", font='arial')
        list_lbl.grid(row=0, column=2)
        
        self.listchoice = IntVar()
        rb_all_book = Radiobutton(list_bar,  text='Short All Books', var=self.listchoice, value=1)
        rb_all_book.grid(row=1, column=0)
        rb_in_stock = Radiobutton(list_bar, text='In stock', var=self.listchoice, value=2)
        rb_in_stock.grid(row=1, column=1)
        rb_issued_book = Radiobutton(list_bar, text='Issued Books', var=self.listchoice, value=3)
        rb_issued_book.grid(row=1, column=2)
        btn_Show_books = Button(
            list_bar, text='Search Books', font='arial')
        btn_Show_books.grid(row=1, column=3, padx=30, pady=10)
        showbooks(self)
        
    def Book(self):
            add = bookwindow.Storebook()
    def new_member(self):
        add = memberwindow.Storemember()
    def issued_book(self):
        add = issuedbookwindow.IssuedBook()
        
def main():
    mainwin = Tk()
    app = Main(mainwin)
    mainwin.title("eLibrary")
    mainwin.geometry('1200x900')
    mainwin.mainloop()


if __name__ == '__main__':
    main()
