from flask import Flask, render_template, request
import sqlite3
import sqlite3 as sql
import mysql.connector
app = Flask(__name__)



con = sqlite3.connect('database.db')
cur = con.cursor()
print ("Opened database successfully")

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

def create_table():

   cur.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
   print ("Table created successfully")

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':

      nm = request.form['nm']
      addr = request.form['addr']
      city = request.form['city']
      pin = request.form['pin']

   with sql.connect("database.db") as con:

        
      cur = con.cursor()
      cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)" , (nm,addr,city,pin))
      con.commit()
      

   return render_template("result.html",msg = msg)
   cur.close()
   con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   con.execute("select * from students")
   
   rows = con.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)