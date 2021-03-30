from flask import Flask, render_template, request, redirect, url_for
from User import User
from Admin import Admin
from Student import Student
from Faculty import Faculty

import mysql.connector

app = Flask(__name__, template_folder = "htmlfiles")

@app.route('/')#whenever you land on this page, login function is called, only the landing page
def login():
	return render_template("loginpage.html")

@app.route('/validate', methods=['POST'])
def validate():
	result = request.form
	email, password = result['email'].lower(),result['password']
	if not(email):#connector.execute(query with %s,args in tuples) - Prevents SQL injections
		return redirect("http://localhost:5000")
	newuser = User(email,password)
	mysqlconnection = mysql.connector.connect(host = "localhost",port=3306, user = "root", database = "pesuapp")
	account_type = newuser.exists(mysqlconnection)
	if account_type:
		if account_type == "admin":
			adminobj=Admin(mysqlconnection,email)
			pass
		if account_type == 'student':
			#return Student(email)
			pass
		if account_type == 'faculty':
			#return Faculty(email)
			pass
	else:
		return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug = True)
