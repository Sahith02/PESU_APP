#faculty table will be ID,email(1* key),Phone number,Address,DateofJoining

class Faculty():
	def __init__(self,email=""):
    	self.email=email
		#get below from the database
		self.FacultyID = id
		self.ContactNumber = phno
		self.Address = address
		self.DateOfJoining = doj
	
	def EditDetails(self,phno = self.phno, address = self.address):
		self.ContactNumber = phno
		self.Address = address
		
	def CheckEventNotification(self,notifications):
		pass

	def __repr__(self):
    	return "\nStudent:\nID = {0}\n".format(self.FacultyID)
	
