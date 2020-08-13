import sqlite3

def create_table():
    conn=sqlite3.connect('/home/martin/Downloads/Python_projects/tkinter section/sqlite/sqlite3.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stationery (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('/home/martin/Downloads/Python_projects/tkinter section/sqlite/sqlite3.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM stationery")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(item,quantity,price):
    conn=sqlite3.connect('/home/martin/Downloads/Python_projects/tkinter section/sqlite/sqlite3.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO stationery VALUES(?,?,?)", (item, quantity,price))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=sqlite3.connect('/home/martin/Downloads/Python_projects/tkinter section/sqlite/sqlite3.db')
    cur=conn.cursor()
    cur.execute("UPDATE stationery SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    conn.commit()
    conn.close()

def delete(item):
    conn=sqlite3.connect('/home/martin/Downloads/Python_projects/tkinter section/sqlite/sqlite3.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM stationery where item=?", (item,))
    conn.commit()
    conn.close()

create_table()
#insert('eraser',30,10)
#update('pencil',8,15)
delete('pencil')
print(view())

