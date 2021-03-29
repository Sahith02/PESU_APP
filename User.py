#user table will have email,pwd and type of user.
#do __init__ first
#Then call login function using User object based on email id
#If exists (based on some check function): return the type of account and also send an object of that type
#If not -> return False

import mysql.connector

class User:
	def __init__(self, password, email):
		self.Password = hash(password)
		self.EmailID = email.lower()
	
	def exists(self,databaseconn):
		#return True
		myc=databaseconn.cursor()
		sqlquery=("SELECT user_type from users where EMAIL=%s and PWD=%s")
		myc.execute(sqlquery,(self.EmailID,self.Password))
		user=myc.fetchall()#will return a tuple a record in database: database order: emailID,pwd and typeofuser
		myc.close()
		if user:
			account_type=user[-1].lower()
		else:
			return False

	def login(self,databaseconn):
		pass
		
		
	def logout(self):
		pass

