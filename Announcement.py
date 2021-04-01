from key_generator.key_generator import generate
import mysql.connector


class Announcement:
	def __init__(self, db_conn, ID = ""):
		
		cur = db_conn.cursor()
		query = "SELECT id, title, location, description, picture_link, hyperlink, posting_time FROM announcement WHERE id = %s"
		cur.execute(query, (ID,))
		result = cur.fetchone()
		# update announcement attributes from database
		self.ID = result[0]
		self.Title = result[1]
		self.Location = result[2]
		self.Description = result[3]
		self.PictureLink = result[4]
		self.HyperLink = result[5]
		self.PostingTime = result[6]

	def __repr__(self):
		return "\nANNOUNCEMENT:\nID = {0} \nTitle = {1} \nLocation = {2} \nDescription = {3} \nPictureLink = {4} \nHyperLink = {5} \nPostingTime = {6}\n".format(
			self.ID, self.Title, self.Location, self.Description, self.PictureLink, self.HyperLink, self.PostingTime)

# A1 = Announcement("1")
# print(A1)
