from flask import Flask, render_template, request, redirect, url_for
from User import User
from Admin import Admin
from Student import Student
from Faculty import Faculty
import mysql.connector

app = Flask(__name__)

@app.route('/') # whenever you land on this page, login function is called, only the landing page
def login():
	return render_template("login_page.html")

@app.route('/validate', methods=['POST'])
def validate():
	return redirect(url_for("student_courses"))

	result = request.form
	email, password = result['email'].lower(), result['password']
	if(not email): # connector.execute(query with %s,args in tuples) - Prevents SQL injections
		return redirect("http://localhost:5000")
	newuser = User(email, password)
	mysqlconnection = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	account_type = newuser.exists(mysqlconnection)
	if(account_type):
		if(account_type == "admin"):
			adminobj = Admin(mysqlconnection, email)
			pass
		if(account_type == 'student'):
			# return Student(email)
			pass
		if(account_type == 'faculty'):
			# return Faculty(email)
			pass
	else:
		return redirect(url_for('login'))

@app.route("/student_courses", methods = ["GET", "POST"])
def student_courses():
	return render_template("student_courses.html")

@app.route("/student_feedback", methods = ["GET", "POST"])
def student_feedback():
	return render_template("student_feedback.html")

@app.route("/student_notifications", methods = ["GET", "POST"])
def student_notifications():
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", password = "", database = "pesuapp")
	A1 = Admin(db_conn, "sahith02@yahoo.com")
	all_announcements = A1.ViewAnnouncements(db_conn)
	return render_template("student_notifications.html", all_announcements = all_announcements)

if __name__ == '__main__':
	app.run(debug = True)
