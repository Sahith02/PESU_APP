#Faculty table will be FacultyID, Name, Email(1* key), ContactNumber, Address, DateofJoining

from Course import Course
from Announcement import Announcement

import mysql.connector
class Faculty():
	def __init__(self,dbconn, email):
		self.cur = dbconn.cursor()
		query = "SELECT * FROM Faculty WHERE Email = %s"
		self.cur.execute(query, (email,))
		res = self.cur.fetchone()
		if res:
			self.FacultyID = res[0]
			self.Name = res[1]
			self.email = res[2]
			self.ContactNumber = res[3]
			self.Address = res[4]
			self.DateOfJoining = res[5]

	def EditDetails(self,db_conn,ContactNumber = None, Address = None):
		self.cur=db_conn.cursor()
		if ContactNumber:
			query = "UPDATE Faculty SET ContactNumber = %s WHERE FacultyID = %s"
			self.cur.execute(query, (ContactNumber,self.FacultyID,))
			db_conn.commit()
		if Address:
			query = "UPDATE Faculty SET Address = %s WHERE FacultyID = %s"
			self.cur.execute(query, (ContactNumber, self.FacultyID,))
			db_conn.commit()
	
	def GetStats(self,db_conn):#to get all the courses the faculty teaches and also total number of students learning that course(not under the faculty)
		cur=db_conn.cursor()
		query="SELECT courseid FROM coufac WHERE facultyid=%s"
		cur.execute(query,(self.FacultyID,))
		res=cur.fetchall()
		nofcourses=len(res)
		courses=[]
		for i in res:
			courseid=i[0]
			query="SELECT count(*) as ncs FROM stucou WHERE courseid=%s"
			cur.execute(query,(courseid,))
			result=cur.fetchone()[0]
			courses.append((Course(db_conn,courseid),result))
		cur.close()
		return (nofcourses,courses)

		
	def ViewAnnouncements(self,db_conn):
		cur = db_conn.cursor()
		query = "SELECT id FROM announcement ORDER BY posting_time DESC"
		cur.execute(query)
		results = cur.fetchall()
		all_announcements = []

		for result in results:
			all_announcements.append(Announcement(db_conn, result[0]))
		return all_announcements
	
	def __del__(self):
		pass

	def __repr__(self):
		return "\nFaculty:\nID = {0}\n".format(self.email)