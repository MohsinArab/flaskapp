import os
from flask import Flask , render_template, request , redirect
from flask_mysqldb import MySQL
import mysql.connector
import yaml


app  = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_POST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] =db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

app.route('/', methods=['GET','POST'])
def Mysql_login():
	if request.method == 'POST':
		userDetails = request.form
		name = userDetails['name']
		email = userDetails['email']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name , email) VALUES(%S , %S) ", (name,email))
		cur.connection.commit()
		cur.close()
		return redirect('/users')
	return render_template('Mysql_login.html')


	app.route('/users')
	def users():
		cur= mysql.connection.cursor()
		result = cur.execute("SELECT * FROM users")
		if result > 0:
			userDetails = cur.fetchall()
			return render_template('users.html' , userDetails= userDetails)



if __name__ == '__main__':
   app.run(debug = True)
