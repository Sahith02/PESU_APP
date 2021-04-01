#Course Table has all info of the courses
#course table: courseid,coursetitle,department,coursedetails,avl
#To establish course-faculty relationship: have a table COUFAC which maps course to faculty COURSEID and FACULTYID
#coufac:facultyid and courseid

class Course():

    def __init__(self,db_conn,CourseID):
        
        self.CourseID=CourseID #cant change it as it is primary key
        cur=db_conn.cursor()
        query="SELECT coursetitle,department,coursedetails,avl FROM course WHERE courseid=%s"
        cur.execute(query,(self.CourseID,))
        result=cur.fetchone()
        CourseTitle,dept,CourseDetails,AVSumm = result
        self.CourseTitle=CourseTitle
        self.Department=dept #the dept the course belongs to
        self.CourseDetails=CourseDetails #a string of all details
        self.AVSummary=AVSumm # First made a single link
        self.faculties=[]
        query="SELECT facultyid FROM coufac WHERE courseid=%s"
        cur.execute(query,(self.CourseID,))
        result=cur.fetchall()#has all faculty ids teaching the subject
        result=[x[0] for x in result]
        query="SELECT `Name`,Email FROM Faculty WHERE FacultyID=%s"
        for i in result:
            cur.execute(query,(i,))
            res=cur.fetchone()
            if res:
                self.faculties.append((res[0],res[1]))#will return (faculty name,facultyemail)
        cur.close()
    
    def __repr__(self):
        return f'''ID: {self.CourseID}\nTitle: {self.CourseTitle}\nDepartment: {self.Department}\nFaculties: {self.faculties}\nCourse Details: {self.CourseDetails}\nAV Summary Links: {self.AVSummary}\n'''

'''
a=Course(123,"abc","CSE",[123],"it is boring","link")
print(a)
'''   
#coufac:courseid,facultyid
#course=id,title,dept,details,AVL
        
