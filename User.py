#user table will have email,pwd(hashed) and type of user.
#do __init__ first
#Then call login function using USer object based on email id
#If exists (based on some check function): return the type of account and also send an object of that type
#If not -> return False

class User:
	def __init__(self, password, email):
		self.Password = password
		self.EmailID = email
	
	def login(self):
    	pass

	def logout(self):
		pass
