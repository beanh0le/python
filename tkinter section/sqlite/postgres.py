import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stationery (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM stationery")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("INSERT INTO stationery VALUES(%s,%s,%s)", (item, quantity,price))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("UPDATE stationery SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("DELETE FROM stationery where item=%s", (item,))
    conn.commit()
    conn.close()

create_table()
#insert('eraser',30,10)
#update('pencil',8,15)
delete('pencil')
print(view())

