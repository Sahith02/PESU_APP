from flask import Flask,render_template,request,redirect
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
	newuser = User(email,password)
	cnx = mysql.connector.connect(host = "localhost", user = "root", database = "mydatabase")
	account_type = newuser.exists(cnx)

	if account_type:
		if account_type == "admin":
			#return Admin(email)
			pass
		if account_type == 'student':
			#return Student(email)
			pass
		if account_type == 'faculty':
			#return Faculty(email)
			pass
	else:
		return redirect("http://localhost:5000")

if __name__ == '__main__':
	app.run(debug = True)
