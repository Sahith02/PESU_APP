#Faculty table will be FacultyID, email(1* key), ContactNumber, Address, DateofJoining

class Faculty():
	def __init__(self, email, dbconn):
		self.cur = dbconn.cursor()
		query = "SELECT * FROM Faculty WHERE email = %s"
		cur.execute(query, (email,))
		res = cur.fetchone()
		self.FacultyID = res[0]
		self.email = res[1]
		self.ContactNumber = res[2]
		self.Address = res[3]
		self.DateOfJoining = res[4]
		
	def EditDetails(self, email = None, ContactNumber = None, Address = None):
		if ContactNumber:
			query = "UPDATE Faculty SET ContactNumber = %s WHERE FacultyID = %s"
			self.cur.execute(query, (ContactNumber,self.FacultyID))
		if Address:
			query = "UPDATE Faculty SET Address = %s WHERE FacultyID = %s"
			self.cur.execute(query, (ContactNumber, self.FacultyID))
		if email:
			query = "UPDATE Faculty SET email = %s WHERE FacultyID = %s"
			self.cur.execute(query, (email , self.FacultyID))
		
	def CheckEventNotification(self,notifications):
		pass
	
	def __del__(self):
		self.cur.close()

	def __repr__(self):
		return "\nStudent:\nID = {0}\n".format(self.email)