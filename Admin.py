#admin table will be ID,email(1* key)

from key_generator.key_generator import generate
import uuid
import mysql.connector
import datetime
from Announcement import Announcement
from Course import Course
from FeedBack import FeedBack
from datetime import datetime

class Admin:
	def __init__(self,db_conn,email = ""):
		cur = db_conn.cursor()
		query = "SELECT id, name FROM `admin` WHERE email = %s"
		cur.execute(query, (email,))
		result = cur.fetchone()
		# update admin attributes from database
		self.ID = result[0]
		self.email = email
		self.name = result[1]
		cur.close()
	
	def AddStudent(self,db_conn,email,srn,name,address,phone,pgm,branch):
		try:
			cur=db_conn.cursor()
			query="SELECT srn from student WHERE srn=%s"
			cur.execute(query,(srn,))
			res=cur.fetchall()
			if res:
				return (False,"Student SRN already exists")
			query="INSERT into student(srn,studname,pgm,emailid,`address`,phonenumber,branch) VALUES (%s,%s,%s,%s,%s,%s,%s)"
			cur.execute(query,(srn,name,pgm,email,address,phone,branch))
			db_conn.commit()
			return (True,"Success")
		except:
			return (False,"Error Connecting to Database")
	
	def AssignStudentToCourse(self,db_conn,studentID,courseID):
		try:
			cursor=db_conn.cursor()
			query="INSERT INTO stucou(courseid,studentid) values (%s,%s)"
			cursor.execute(query,(courseID,studentID,))
			db_conn.commit()
			cursor.close()
			return True
		except:
			print(f"\nError while assigning Student-{studentID} to Course-{courseID}\n")
			return False

	def EditStudent(self,db_conn,srn="",name="",address="",phone="",branch="",courses=[]):
		if srn:
			cur=db_conn.cursor()
			query="SELECT studname FROM student where srn=%s"
			cur.execute(query,(srn,))
			res=cur.fetchall()
			if not(res):
				return (False,"Student Does Not Exist")
			if address:
				query="UPDATE student SET address=%s WHERE srn=%s"
				cur.execute(query,(address,srn,))
				db_conn.commit()
			if name:
				query="UPDATE student SET studname=%s WHERE srn=%s"
				cur.execute(query,(name,srn,))
				db_conn.commit()
			if phone:
				query="UPDATE student SET phonenumber=%s WHERE srn=%s"
				cur.execute(query,(phone,srn,))
				db_conn.commit()
			if branch:
				query="UPDATE student SET branch=%s WHERE srn=%s"
				cur.execute(query,(branch,srn,))
				db_conn.commit()
			cur.close()
			if courses:
				for courseid in courses:
					self.AssignStudentToCourse(db_conn,srn,courseid)
			return (True,"Done")
		else:
			return (False,"Student Does Not Exist")
			

	def AddFaculty(self,db_conn,email,id,name,address,phone,date):
		try:
			cur=db_conn.cursor()
			query="SELECT `FacultyID` from faculty WHERE FacultyID=%s"
			cur.execute(query,(id,))
			res=cur.fetchall()
			if res:
				return (False,"Faculty ID already exists")
			date=datetime.strptime(date,"%Y-%m-%d")
			query="INSERT into faculty(FacultyID,`Name`,Email,ContactNumber,`Address`,DateOfJoining) VALUES (%s,%s,%s,%s,%s,%s)"
			cur.execute(query,(id,name,email,phone,address,date))
			db_conn.commit()
			return (True,"Success")
		except Exception as E:
			print(E)
			return (False,"Error Connecting to Database")

	def EditFaculty(self,db_conn,id,name,address,phonenumber,courseid):
		if id:
			cur=db_conn.cursor()
			query="SELECT `Name` FROM faculty where FacultyID=%s"
			cur.execute(query,(id,))
			res=cur.fetchall()
			if not(res):
				return (False,"Faculty Does Not Exist")
			if address:
				query="UPDATE faculty SET `address`=%s WHERE FacultyID=%s"
				cur.execute(query,(address,id,))
				db_conn.commit()
			if name:
				query="UPDATE faculty SET `Name`=%s WHERE FacultyID=%s"
				cur.execute(query,(name,id,))
				db_conn.commit()
			if phonenumber:
				query="UPDATE faculty SET ContactNumber=%s WHERE FacultyID=%s"
				cur.execute(query,(phonenumber,id,))
				db_conn.commit()
			cur.close()
			if courseid:
				for i in courseid:
					self.AssignFacultyToCourse(db_conn,id,i)
			return (True,"Done")
		else:
			return (False,"Faculty Does Not Exist")

	def AssignFacultyToCourse(self,db_conn,facultyID,courseID):
		try:
			cursor=db_conn.cursor()
			query="INSERT INTO coufac(courseid,facultyid) values (%s,%s)"
			cursor.execute(query,(courseID,facultyID,))
			db_conn.commit()
			cursor.close()
			return True
		except:
			print(f"\nError while assigning Faculty-{facultyID} to Course-{courseID}\n")
			return False

	def ViewCourse(self,db_conn,id=""):
		cur=db_conn.cursor()
		query="SELECT courseid FROM course"
		cur.execute(query)
		res=cur.fetchall()
		cur.close()
		courses=[]
		if res:
			courses=[Course(db_conn,x[0]) for x in res]
		return courses

	def AddCourse(self,db_conn,ID,CourseTitle="",Department="",Faculties=[],Details="",AVSummary=""):
		#db_conn is the database connection, Faculties is list of faculty ids
		
		if ID and CourseTitle and Department and Faculties and Details and AVSummary:
			try:
				cur = db_conn.cursor()
				query="SELECT * FROM course WHERE courseid=%s"
				cur.execute(query,(ID,))
				res=cur.fetchall()
				if res:
					return (False,("Course Already Exists"))
				query="INSERT INTO course(courseid,coursetitle,department,coursedetails,avl) values(%s,%s,%s,%s,%s)"
				cur.execute(query,(ID,CourseTitle,Department,Details,AVSummary,))
				db_conn.commit()
				for facultyid in Faculties:
					k=self.AssignFacultyToCourse(db_conn,facultyid,ID)
					if not(k):
						break
				return (True,"All Done")
			except Exception as E:
				print(E)
				#print("\nError in adding the course\n")
				return (False,"Error connecting to database")
		else:
			return (False,"Not all details given")

	def EditCourse(self,db_conn,Id="",Title="",Facultiestobeadded=[],Details="",AVS=""):#dept can't change
		#faculties can only be added
		if Id:
			cur=db_conn.cursor()
			query="SELECT * FROM course WHERE courseid=%s"
			cur.execute(query,(Id,))
			res=cur.fetchall()
			if not res:
					return (False,("Course Does Not Exist"))
			if Title:
				query="UPDATE course SET coursetitle=%s WHERE courseid=%s"
				cur.execute(query,(Title,Id,))
				db_conn.commit()
			if Details:
				query="UPDATE course SET coursedetails=%s WHERE courseid=%s"
				cur.execute(query,(Details,Id,))
				db_conn.commit()
			if AVS:
				query="UPDATE course SET avl=%s WHERE courseid=%s"
				cur.execute(query,(AVS,Id,))
				db_conn.commit()
			cur.close()
			if Facultiestobeadded:
				for i in Facultiestobeadded:
					self.AssignFacultyToCourse(i,Id,db_conn)
			return (True,"Done")
		else:
			return (False,"Course Does Not Exist")

	def ViewAnnouncements(self,db_conn):
		cur = db_conn.cursor()
		query = "SELECT id FROM announcement ORDER BY posting_time DESC"
		cur.execute(query)
		results = cur.fetchall()
		all_announcements = []

		for result in results:
			all_announcements.append(Announcement(db_conn, result[0]))
		return all_announcements

	def AddAnnouncement(self, db_conn, ID = None, Title = "", Location = "", Description = "", PictureLink = "", HyperLink = "", PostingTime = None):
		ID = generate(num_of_atom = 1, min_atom_len = 10, max_atom_len = 10).get_key() if (ID == None) else ID
		PostingTime = datetime.datetime.now() if (PostingTime == None) else PostingTime
		cur = db_conn.cursor()
		query = "INSERT INTO `pesuapp`.`announcement` (`id`, `title`, `location`, `description`, `picture_link`, `hyperlink`, `posting_time`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
		cur.execute(query, (ID, Title, Location, Description, PictureLink, HyperLink, PostingTime,))
		db_conn.commit()
		cur.close()

	def UpdateAnnouncement(self,db_conn, ID = None, Title = None, Location = None, Description = None, PictureLink = None, HyperLink = None):
		
		if(ID):
			cur = db_conn.cursor()
			if(Title):
				query = "UPDATE announcement SET title = %s WHERE id = %s"
				# print(Title, ID)
				cur.execute(query, (Title, ID,))
				db_conn.commit()
			if(Location):
				query = "UPDATE announcement SET location = %s WHERE id = %s"
				cur.execute(query, (Location, ID,))
				db_conn.commit()
			if(Description):
				query = "UPDATE announcement SET description = %s WHERE id = %s"
				cur.execute(query, (Description, ID,))
				db_conn.commit()
			if(PictureLink):
				query = "UPDATE announcement SET picture_link = %s WHERE id = %s"
				cur.execute(query, (PictureLink, ID,))
				db_conn.commit()
			if(HyperLink):
				query = "UPDATE announcement SET hyperlink = %s WHERE id = %s"
				cur.execute(query, (HyperLink, ID,))
				db_conn.commit()
		else:
			return
	
	def RemoveAnnouncement(self, db_conn, ID = None):
		if(ID == None):
			return
		else:
			cur = db_conn.cursor()
			query = "DELETE FROM announcement WHERE id = %s"
			cur.execute(query, (ID, ))
			db_conn.commit()
	
	def ViewFeedback(self, db_conn, CourseID = ""):
		if(not CourseID):
			return []
		else:
			cur = db_conn.cursor()
			query = "SELECT CourseID, StudentID, Review FROM feedback WHERE CourseID = %s"
			cur.execute(query, (CourseID, ))
			results = cur.fetchall()
			all_feedback = []
			for feedback in results:
				all_feedback.append({"CourseID": feedback[0], "StudentID": feedback[1], "Review": feedback[2]})
			return all_feedback

	def __repr__(self):
		return "\nADMIN:\nID = {0}\nEmail = {1}\nName = {2}".format(self.ID, self.email, self.name)

# A1 = Admin("sahith02@yahoo.com")
# print(A1)

# code to remove an announcement with ID
# A1.RemoveAnnouncement(ID = "4")

# code to update an annoucement
# A1.UpdateAnnouncement(ID = "4", Title = "title 4", Location = "location 4", Description = "description 4", PictureLink = "picture link 4", HyperLink = "hyperlink 4")

# code to add a new announcement - [CAUTION] It changes the original database
# A1.AddAnnouncement(ID = "4", Title = "Title 4")

# print all announcements
# all_announcements = A1.ViewAnnouncements()
# for announcement in all_announcements:
# 	print(announcement)
