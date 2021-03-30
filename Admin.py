#admin table will be ID,email(1* key)

from key_generator.key_generator import generate
import mysql.connector
import datetime
from Announcement import Announcement

class Admin:
	def __init__(self, email = ""):
		# start database connection
		self.db_conn = mysql.connector.connect(
			host = "localhost",
			port = 3306,
			user = "root",
			password = "root",
			database = "pesuapp"
		)
		# query details from database
		cur = self.db_conn.cursor()
		query = "SELECT id, name FROM admin WHERE email = %s"
		cur.execute(query, (email,))
		result = cur.fetchone()
		# update admin attributes from database
		self.ID = result[0]
		self.email = email
		self.name = result[1]
	
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

	def AddAnnouncement(self, ID = None, Title = "", Location = "", Description = "", PictureLink = "", HyperLink = "", PostingTime = None):
		ID = generate(num_of_atom = 1, min_atom_len = 10, max_atom_len = 10).get_key() if (ID == None) else ID
		PostingTime = datetime.datetime.now() if (PostingTime == None) else PostingTime
		cur = self.db_conn.cursor()
		query = "INSERT INTO `pesuapp`.`announcement` (`id`, `title`, `location`, `description`, `picture_link`, `hyperlink`, `posting_time`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
		cur.execute(query, (ID, Title, Location, Description, PictureLink, HyperLink, PostingTime))
		self.db_conn.commit()

	def ViewAnnouncements(self):
		cur = self.db_conn.cursor()
		query = "SELECT id FROM announcement ORDER BY posting_time DESC"
		cur.execute(query)
		results = cur.fetchall()
		all_announcements = []
		for result in results:
			all_announcements.append(Announcement(result[0]))
		return all_announcements

	def AssignFacultyToCourse(self):
		pass

	def __repr__(self):
		return "\nADMIN:\nID = {0}\nEmail = {1}\nName = {2}".format(self.ID, self.email, self.name)

A1 = Admin("sahith02@yahoo.com")
print(A1)

# print all announcements
all_announcements = A1.ViewAnnouncements()
for announcement in all_announcements:
	print(announcement)

# code to add a new announcement - [CAUTION] It changes the original database
# A1.AddAnnouncement(ID = "4", Title = "Title 4")