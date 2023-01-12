import sqlite3

class Database:
	def create_table(name):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS %s (item TEXT , quantity INTEGER , value REAL )" %(name))
	conn.commit()
	conn.close()

	def insert(item , quantity , value):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(? , ? , ?)" , (item , quantity , value))
	conn.commit()
	conn.close()

	def view(name , item):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM %s WHERE item = ?" %(name) ,(item,))
	rows = cur.fetchall()
	conn.close()
	return rows

	def update(quantity , value , item):
	conn = sqlite.connect('lite.db')
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity = ? , value = ? WHERE item = ?" , (quantity , value , item))
	conn.commit()
	conn.close()

	def delete(item):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM store where item = ?" , (item,))
	conn.commit()
	conn.close()

print(view('store' , 'Iphone 6'))

