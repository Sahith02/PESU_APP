from flask import Flask,render_template,request,redirect
from User import User
app = Flask(__name__,template_folder="htmlfiles")

@app.route('/')#whenever you land on this page, login function is called, only the landing page
def login():
	return render_template("loginpage.html")

@app.route('/loggedin',methods=['POST'])
def validate():
	result=request.form
	newuser=User(result['email'],result['password'])
	obj=newuser.exists("abc")
	if obj:
		return "HELLO"
		obj.login()
	else:
		return redirect("http://localhost:5000")


if __name__ == '__main__':
	app.run(debug=True)