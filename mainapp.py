from flask import Flask,render_template,request,redirect
from User import User
from Admin import Admin
from Student import Student
from Faculty import Faculty
app = Flask(__name__,template_folder="htmlfiles")

@app.route('/')#whenever you land on this page, login function is called, only the landing page
def login():
	return render_template("loginpage.html")

@app.route('/loggedin',methods=['POST'])
def validate():
	result=request.form
	email,password=result['email'].lower(),result['password']
	newuser=User(email,password)
	obj=newuser.exists("abc")#newuser.exists(mysql connection)
	account_type=obj
	if obj:
		if account_type=="admin":
				return Admin(email)
		if account_type=='student':
				return Student(email)
		if account_type=='faculty':
				return Faculty(email)
	else:
		return redirect("http://localhost:5000")


if __name__ == '__main__':
	app.run(debug=True)