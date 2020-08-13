import sqlite3

class Database:
    def __init__(self):
        self.conn=sqlite3.connect('/home/martin/Downloads/Python_projects/tkinter section/Bookstore app/books.db')
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
      
    def insert(self,title='', author='', year='', isbn=''):
        self.cur.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM bookstore WHERE id=?", (id,))
        self.conn.commit()
        
    def search(self,title='', author='', year='', isbn=''):
        self.cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def update(self,id,title, author, year, isbn):
        self.cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        
#connect()
#insert("The Lord of the Rings", "JRR Tolkien", 1980, 1234358534)
#delete(6)
#update(4,"Happy Potter", "JK Rowling", 1998, 1234)
#print(view())
#print(search('JK Rowling'))