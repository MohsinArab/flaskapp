import sqlite3

con = sqlite3.connect('database.py')
print ("Opened database successfully")

con.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created successfully")
conn.close()