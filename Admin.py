from key_generator.key_generator import generate

class Admin:
	def __init__(self, ID = None):
		self.ID = generate(num_of_atom = 1, min_atom_len = 10, max_atom_len = 10).get_key() if (ID == None) else ID
	
	def AddStudent(self):
		pass

	def EditStudent(self):
		pass

	def AddFaculty(self):
		pass

	def EditFaculty(self):
		pass

	def AddCourse(self):
		pass

	def EditCourse(self):
		pass

	def AddAnnouncement(self):
		pass

	def AssignFacultyToCourse(self):
		pass

	def SendAnnouncement(self):
		pass

	def __repr__(self):
		return "\nADMIN:\nID = {0}\n".format(self.ID)

A1 = Admin()
print(A1)