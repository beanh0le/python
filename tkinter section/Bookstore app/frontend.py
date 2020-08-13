from tkinter import *
from backend import Database

database = Database()

class Frontend:

    def __init__(self):
        self.l1=Label(window,text='Title')
        self.l1.grid(row=0,column=0)

        self.l2=Label(window,text='Author')
        self.l2.grid(row=0,column=2)

        self.l3=Label(window,text='Year')
        self.l3.grid(row=1,column=0)

        self.l4=Label(window,text='ISBN')
        self.l4.grid(row=1,column=2)

        self.title_value=StringVar()
        self.e1=Entry(window,textvariable=self.title_value)
        self.e1.grid(row=0, column=1)

        self.author_value=StringVar()
        self.e2=Entry(window,textvariable=self.author_value)
        self.e2.grid(row=0, column=3)

        self.year_value=StringVar()
        self.e3=Entry(window,textvariable=self.year_value)
        self.e3.grid(row=1, column=1)

        self.isbn_value=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        self.lb1=Listbox(window,height=8,width=30)
        self.lb1.grid(row=2,column=0,rowspan=7,columnspan=2)

        self.lb1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2,column=2,rowspan=5,columnspan=1)

        self.sb2=Scrollbar(window, orient=HORIZONTAL)
        self.sb2.grid(row=8,column=0,rowspan=1,columnspan=2)

        self.lb1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.lb1.yview)

        self.lb1.configure(xscrollcommand=self.sb2.set)
        self.sb2.configure(command=self.lb1.xview)

        self.b1=Button(window,text='View All',width=10, command=self.view_all)
        self.b1.grid(row=2, column=3)

        self.b2=Button(window,text='Search Entry',width=10, command=self.search_entry)
        self.b2.grid(row=3, column=3)

        self.b3=Button(window,text='Add Entry',width=10, command=self.add_entry)
        self.b3.grid(row=4, column=3)

        self.b4=Button(window,text='Update',width=10, command=self.update_selected)
        self.b4.grid(row=5, column=3)

        self.b5=Button(window,text='Delete',width=10, command=self.delete_selected)
        self.b5.grid(row=6, column=3)

        self.b6=Button(window,text='Close',width=10, command=window.destroy)
        self.b6.grid(row=7, column=3)

    def get_selected_row(self,event):
        try:
            #global selected_entry
            index = self.lb1.curselection()
            self.selected_entry = self.lb1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END, self.selected_entry[1])
            self.e2.delete(0,END)
            self.e2.insert(END, self.selected_entry[2])
            self.e3.delete(0,END)
            self.e3.insert(END, self.selected_entry[3])
            self.e4.delete(0,END)
            self.e4.insert(END, self.selected_entry[4])
        except IndexError:
            pass
        
    def delete_selected(self):
        database.delete(self.selected_entry[0])

    def update_selected(self):
        database.update(self.selected_entry[0],self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())

    def view_all(self):
        self.lb1.delete(0,END)
        for row in database.view():
            self.lb1.insert(END, row)

    def search_entry(self):
        self.lb1.delete(0,END)
        for row in database.search(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()):
            self.lb1.insert(END, row)

    def add_entry(self):
        database.insert(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.lb1.delete(0,END)
        self.lb1.insert(END, (self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()))


window=Tk()
frontend = Frontend()
window.title('BookStore')
window.mainloop()