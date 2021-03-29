import mysql.connector

#FeedBack table -> CourseID, StudentID, Review

class FeedBack:
	def __init__(self, course, student):
		self.CourseID = course
		self.StudentID = student
		self.Review = None
	
	def ViewReview(self, dbconn):
		#cnx = mysql.connector.connect(host = "localhost", user = "root", database = "mydatabase")
		cur = dbconn.cursor()
		q = "SELECT * FROM FeedBack WHERE CourseID = %s AND StudentID = %s"
		cur.execute(q, (self.CourseID, self.StudentID))
		res = cur.fetchone()
		self.Review = res[2]
		return self.Review
	
	def WriteReview(self, review, dbconn):
		self.Review = review
		try:
			#cnx = mysql.connector.connect(host = "localhost", user = "root", database = "mydatabase")
			cur = dbconn.cursor()
			q = "INSERT INTO FeedBack VALUES(%s, %s, %s)"
			cur.execute(q, (self.CourseID, self.StudentID, review))
			return True
		except:
			return False