import sqlite3 , os

os.chdir("C:\\Users\\pc\\Documents\\Python Practices")

def create_table():
	connect = sqlite3.connect('database.db')

	cur = connect.cursor()

	cur.execute('CREATE TABLE IF NOT EXISTS Car(CarID text , CarModel text, CarMake text, CarYear  int)')
	cur.execute('INSERT INTO Car VALUES("C1" , "C2" , "Toyota" , 2016)')
	cur.ext

	connect.commit()

def insert_value():
	connect = sqlite3.connect('database.db')
	cur = connect.cursor()
	cur.execute('INSERT INTO Car VALUES("C1" , "C2" , "Toyota" , 2016)')
	connect.commit()
	connect.close()


def view():
	connect = sqlite3.connect('database.db')

	cur = connect.cursor()



