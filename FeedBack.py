import mysql.connector
#FeedBack table -> CourseID, StudentID, Review

class FeedBack:
	def __init__(self, course, student, dbconn):
		self.cur = dbconn.cursor()
		self.CourseID = course
		self.StudentID = student
		self.Review = None
	
	def ViewReview(self):
		q = "SELECT * FROM FeedBack WHERE CourseID = %s AND StudentID = %s"
		self.cur.execute(q, (self.CourseID, self.StudentID))
		res = self.cur.fetchone()
		self.Review = res[2]
		return self.Review
	
	def WriteReview(self, review, dbconn):
		self.Review = review
		try:
			q = "INSERT INTO FeedBack VALUES(%s, %s, %s)"
			self.cur.execute(q, (self.CourseID, self.StudentID, review))
			return True
		except:
			return False

	def __del__(self):
		self.cur.close()