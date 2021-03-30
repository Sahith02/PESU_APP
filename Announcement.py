from key_generator.key_generator import generate
import mysql.connector


class Announcement:
	def __init__(self, ID = ""):
		# start database connection
		self.db_conn = mysql.connector.connect(
			host = "localhost",
			port = 3306,
			user = "root",
			password = "root",
			database = "pesuapp"
		)
		# get details from database
		cur = self.db_conn.cursor()
		q = "SELECT id, title, location, description, picture_link, hyperlink, posting_time FROM announcement WHERE id = %s"
		cur.execute(q, (ID,))
		res = cur.fetchone()
		print(res)
		# update announcement attributes from database
		self.ID = res[0]
		self.Title = res[1]
		self.Location = res[2]
		self.Description = res[3]
		self.PictureLink = res[4]
		self.HyperLinks = res[5]
		self.PostingTime = res[6]
	
	def ViewAnnouncements(self):
		pass

	def __repr__(self):
		return "\nANNOUNCEMENT:\nID = {0} \nTitle = {1} \nLocation = {2} \nDescription = {3} \nPictureLink = {4} \nHyperLinks = {5} \nPostingTime = {6}\n".format(
			self.ID, self.Title, self.Location, self.Description, self.PictureLink, self.HyperLinks, self.PostingTime)

A1 = Announcement("1")
print(A1)
