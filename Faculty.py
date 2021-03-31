#Faculty table will be FacultyID, Name, Email(1* key), ContactNumber, Address, DateofJoining

class Faculty():
	def __init__(self, email, dbconn):
		self.cur = dbconn.cursor()
		query = "SELECT * FROM Faculty WHERE email = %s"
		self.cur.execute(query, (email,))
		res = self.cur.fetchone()
		if res:
			self.FacultyID = res[0]
			self.Name = res[1]
			self.email = res[2]
			self.ContactNumber = res[3]
			self.Address = res[4]
			self.DateOfJoining = res[5]

	def EditDetails(self, email = None, ContactNumber = None, Address = None):
		if ContactNumber:
			query = "UPDATE Faculty SET ContactNumber = %s WHERE FacultyID = %s"
			self.cur.execute(query, (ContactNumber,self.FacultyID))
		if Address:
			query = "UPDATE Faculty SET Address = %s WHERE FacultyID = %s"
			self.cur.execute(query, (ContactNumber, self.FacultyID))
		if email:
			query = "UPDATE Faculty SET Email = %s WHERE FacultyID = %s"
			self.cur.execute(query, (email , self.FacultyID))
		
	def CheckEventNotification(self, notifications):
		pass
	
	def __del__(self):
		self.cur.close()

	def __repr__(self):
		return "\nStudent:\nID = {0}\n".format(self.email)