from flask import Flask, render_template, request, redirect, url_for,session
from User import User
from Admin import Admin
from Announcement import Announcement
from Student import Student
from Faculty import Faculty
import mysql.connector

app = Flask(__name__)
app.secret_key="saresr"

@app.route('/') # whenever you land on this page, login function is called, only the landing page
def login():
	return render_template("login_page.html",error = None)

@app.route('/validate', methods=['POST'])
def validate():
	#return redirect(url_for("student_courses"))
	result = request.form
	email, password = result['email'].lower(), result['password']
	# if(not email): # connector.execute(query with %s,args in tuples) - Prevents SQL injections
	# 	return redirect("http://localhost:5000")
	newuser = User(email, password)
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	account_type = newuser.exists(db_conn)
	session['email']=""
	session['type']=""
	if(account_type):
		if(account_type == "admin"):
			session['email']=email
			session['type']="admin"
			#session['obj']=Admin(db_conn, email)
			#return redirect(url_for("student_courses"))
			#adminobj = Admin(db_conn, email)

		if(account_type == 'student'):
			session['email']=email
			session['type']="student"
			#session['obj']=Student(db_conn, email)
			return redirect(url_for("student_courses"))
			# return Student(email)

		if(account_type == 'faculty'):
			# return Faculty(email)
			session['email']=email
			session['type']="faculty"
			#session['obj']=Faculty(db_conn, email)
			return redirect(url_for("faculty_courses"))
	else:
		session.pop('email',None)
		session.pop('type',None)
		error = "Invalid email id or password"
		return render_template("login_page.html",error = error)#redirect(url_for('login',error=error))

@app.route("/student_courses", methods = ["GET", "POST"])
def student_courses():
	try:
		if session['type']!="student":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	S1 = Student(db_conn, session['email'])
	courses_enrolled = S1.ViewCourses(db_conn)
	return render_template("student_courses.html", courses_enrolled = courses_enrolled)

@app.route("/sendfeedback",methods=["POST","GET"])
def sendfeedback():
	pass

@app.route("/student_feedback", methods = ["GET", "POST"])
def student_feedback():
	try:
		if session['type']!="student":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	S1 = Student(db_conn, session['email'])
	courses_enrolled = S1.ViewCourses(db_conn)
	#courses_enrolled = session['obj'].ViewCourses(db_conn)
	return render_template("student_feedback.html",studid=S1.srn,courses_enrolled=courses_enrolled)

@app.route("/student_notifications", methods = ["GET", "POST"])
def student_notifications():
	try:
		if session['type']!="student":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	A1 = Student(db_conn, session['email'])
	all_announcements = A1.ViewAnnouncements(db_conn)
	#all_announcements = session['obj'].ViewAnnouncements(db_conn)
	return render_template("student_notifications.html", all_announcements = all_announcements)

@app.route("/student_notification/<string:ID>", methods = ["GET", "POST"])
def student_notification(ID = ""):
	try:
		if session['type']!="student":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	announcement = Announcement(db_conn, ID)
	return render_template("student_notification.html", announcement = announcement)

@app.route("/faculty_courses",methods=["GET","POST"])
def faculty_courses():
	try:
		if session['type']!="faculty":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	F1=Faculty(db_conn,session['email'])
	number_of_courses,course_list=F1.GetStats(db_conn)
	#number_of_courses,course_list=session['obj'].GetStats(db_conn)
	return render_template("faculty_courses.html",number_of_courses=number_of_courses,course_list=course_list)

@app.route("/faculty_notifications", methods = ["GET", "POST"])
def faculty_notifications():
	try:
		if session['type']!="faculty":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	A1 = Faculty(db_conn, session['email'])
	all_announcements = A1.ViewAnnouncements(db_conn)
	#all_announcements = session['obj'].ViewAnnouncements(db_conn)
	return render_template("faculty_notifications.html", all_announcements = all_announcements)

@app.route("/faculty_notification/<string:ID>", methods = ["GET", "POST"])
def faculty_notification(ID = ""):
	try:
		if session['type']!="faculty":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	announcement = Announcement(db_conn, ID)
	return render_template("faculty_notification.html", announcement = announcement)

@app.route("/log",methods=["GET","POST"])
def logout():
	session.pop('email',None)
	session.pop('type',None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug = True)
