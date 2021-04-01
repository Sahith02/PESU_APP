#user table will have email,pwd and type of user.
#do __init__ first
#Then call login function using User object based on email id
#If exists (based on some check function): return the type of account and also send an object of that type
#If not -> return False

import mysql.connector
from passlib.hash import sha256_crypt

class User:
	def __init__(self,email, password):
		self.Password = password
		self.EmailID = email.lower()
	
	def exists(self, databaseconn):
		cur = databaseconn.cursor()
		query = "SELECT `password`,`account_type` FROM users WHERE email=%s"
		cur.execute(query,(self.EmailID,))
		result=cur.fetchone()
		if result:
			if (sha256_crypt.verify(self.Password,result[0])):
				return result[1]
			else:
				return False
		return False		

	def login(self):
		pass
		
	def logout(self):
		pass

