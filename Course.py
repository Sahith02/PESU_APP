#Course Table has all info of the courses
#To establish course-faculty relationship: have a table COUFAC which maps course to faculty COURSEID and FACULTYID

class Course():

    def __init__(self,CourseID,CourseTitle,dept,Faculties,CourseDetails,AVSumm):
        
        self.CourseTitle=CourseTitle
        self.CourseID=CourseID #cant change it as it is primary key
        self.Department=dept #the dept the course belongs to
        self.Faculties=Faculties #the list of faculties handling the course
        self.CourseDetails=CourseDetails #a string of all details
        self.AVSummary=AVSumm # First made a single link
        #list of links using JSON type in MySQL
    
    def __repr__(self):
        return f'''ID: {self.CourseID}\nTitle: {self.CourseTitle}\nDepartment: {self.Department}\nFaculties: {self.Faculties}\nCourse Details: {self.CourseDetails}\nAV Summary Links: {self.AVSummary}\n'''

'''
a=Course(123,"abc","CSE",[123],"it is boring","link")
print(a)
'''   
#coufac:courseid,facultyid
#course=id,title,dept,details,AVL
        
