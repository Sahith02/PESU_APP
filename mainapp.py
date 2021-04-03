from flask import Flask, render_template, request, redirect, url_for,session
from User import User
from Admin import Admin
from Announcement import Announcement
from Student import Student
from Faculty import Faculty
from FeedBack import FeedBack
import mysql.connector
from passlib.hash import sha256_crypt

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
			return redirect(url_for("admin_notifications"))
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
	print("here")
	try:
		if session['type']!="student":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	S1=Student(db_conn, session['email'])
	courses_enrolled = S1.ViewCourses(db_conn)
	result=request.form
	notifs={}
	for course in courses_enrolled:
		ID=course.CourseID
		if result[str(ID)]:
			notifs[ID]=result[str(ID)]
	for i in notifs:
		F1=FeedBack(i,S1.srn)
		print(F1.WriteReview(notifs[i],db_conn))
		del F1	
	return redirect(url_for("student_courses"))

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

@app.route("/admin_courses", methods=["GET","POST"])
def admin_courses():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	cur=db_conn.cursor()
	query="SELECT courseid,coursetitle FROM course"
	cur.execute(query)
	res=cur.fetchall()
	return render_template("admin_courses.html", courses = res)

@app.route("/courseadd",methods=["GET","POST"])
def courseadd():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	result=request.form
	id,title,dept,avl,details,faculties=result['CourseID'],result['CourseTitle'],result['Department'],result['AVL'],result['CourseDetails'],result['FID']
	faculties=faculties.split(",")
	faculties=[x.strip() for x in faculties]
	A1=Admin(db_conn,session['email'])
	k=A1.AddCourse(db_conn,id,title,dept,faculties,details,avl)

	#for pushing to courses site
	cur=db_conn.cursor()
	query="SELECT courseid,coursetitle FROM course"
	cur.execute(query)
	res=cur.fetchall()
	if k[0]:
		return render_template("admin_courses.html",courses=res,success="Successfully Added")
	else:
		return render_template("admin_courses.html",courses=res,error=k[1])


@app.route("/add_course",methods=["GET","POST"])
def add_course():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	#db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return render_template("add_course.html")

@app.route("/courseedit",methods=["GET","POST"])
def courseedit():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	result=request.form
	id,title,avl,details,faculties=result['CourseID'],result['CourseTitle'],result['AVL'],result['CourseDetails'],result['FID']
	faculties=faculties.split(",")
	faculties=[x.strip() for x in faculties]
	A1=Admin(db_conn,session['email'])
	k=A1.EditCourse(db_conn,id,title,faculties,details,avl)
	
	#for pushing to courses site
	cur=db_conn.cursor()
	query="SELECT courseid,coursetitle FROM course"
	cur.execute(query)
	res=cur.fetchall()
	if k[0]:
		return render_template("admin_courses.html",courses=res,success="Successfully Added")
	else:
		return render_template("admin_courses.html",courses=res,error=k[1])

@app.route("/edit_course",methods=["GET","POST"])
def edit_course():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	#db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return render_template("edit_course.html")

@app.route("/admin_notifications", methods = ["GET", "POST"])
def admin_notifications():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	A1 = Admin(db_conn, session['email'])
	all_announcements = A1.ViewAnnouncements(db_conn)
	#all_announcements = session['obj'].ViewAnnouncements(db_conn)
	return render_template("admin_notifications.html", all_announcements = all_announcements)

@app.route("/admin_notification/<string:ID>", methods = ["GET", "POST"])
def admin_notification(ID = ""):
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	# db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root", database = "pesuapp")
	announcement = Announcement(db_conn, ID)
	return render_template("admin_notification.html", announcement = announcement)

@app.route("/add_notification",methods=["GET","POST"])
def add_notification():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return render_template("add_notification.html")

@app.route("/edit_notification",methods=["GET","POST"])
def edit_notification():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return "hello"

@app.route("/admin_students",methods=["GET","POST"])
def admin_students():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	db_conn=mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	cur=db_conn.cursor()
	query="SELECT srn,studname FROM student"
	cur.execute(query)
	res=cur.fetchall()
	return render_template("admin_students.html", students = res)

@app.route("/studentadd",methods=["GET","POST"])
def studentadd():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	result=request.form
	srn,name,pgm,address,phone,branch=result["StudentSRN"],result["StudentName"],result["Program"],result["Address"],result["StudentPhone"],result["Branch"]
	email,passw,repassw=result["email"],result["password"],result["repassword"]
	error,success="",""
	if passw!=repassw:
		error="Passwords Don't Match!"
	else:
		db_conn=mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
		cur=db_conn.cursor()
		A1=Admin(db_conn,session['email'])
		k=A1.AddStudent(db_conn,email,srn,name,address,phone,pgm,branch)
		if k[0]:
			success=k[1]
			acct_type='student'
			passw=sha256_crypt.hash(passw)
			query="INSERT INTO users(`password`,account_type,email) VALUES(%s,%s,%s)"
			cur.execute(query,(passw,acct_type,email,))
			db_conn.commit()
		else:
			error=k[1]
	db_conn=mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	cur=db_conn.cursor()
	query="SELECT srn,studname FROM student"
	cur.execute(query)
	res=cur.fetchall()
	if success:
		return render_template("admin_students.html",students=res,success="Successfully Added")
	return render_template("admin_students.html",students=res,error=error)

@app.route("/add_student",methods=["GET","POST"])
def add_student():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	#db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return render_template("add_student.html")

@app.route("/studentedit",methods=["GET","POST"])
def studentedit():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	result=request.form
	id,name,address,phonenumber,branch,courseid=result['StudentID'],result['StudentName'],result['Address'],result['Phone'],result['Branch'],result['CID']
	courseid=courseid.split(",")
	courseid=[x.strip() for x in courseid]
	db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	A1=Admin(db_conn,session['email'])
	k=A1.EditStudent(db_conn,id,name,address,phonenumber,branch,courseid)
	cur=db_conn.cursor()
	query="SELECT srn,studname FROM student"
	cur.execute(query)
	res=cur.fetchall()
	if k[0]:
		return render_template("admin_students.html",students=res,success="Successfully Edited")
	return render_template("admin_students.html",students=res,error=k[1])


@app.route("/edit_student",methods=["GET","POST"])
def edit_student():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	#db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return render_template("edit_student.html")

@app.route("/add_faculty",methods=["GET","POST"])
def add_faculty():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	#db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return "hello"

@app.route("/edit_faculty",methods=["GET","POST"])
def edit_faculty():
	try:
		if session['type']!="admin":
			return redirect(url_for("logout"))
	except:
		return redirect(url_for("logout"))
	#db_conn = mysql.connector.connect(host = "localhost", port = 3306, user = "root",password="root", database = "pesuapp")
	return "hello"

@app.route("/log",methods=["GET","POST"])
def logout():
	session.pop('email',None)
	session.pop('type',None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug = True)
