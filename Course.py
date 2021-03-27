#Course Table has all info of the courses
#To establish course-faculty relationship: have a table COUFAC which maps course to faculty COURSEID and FACULTYID

class Course():

    def __init__(self,CourseTitle,CourseID,dept,Faculties,CourseDetails,\
        AVSumm,Units):
        
        self._CourseTitle=CourseTitle
        self._CourseID=CourseID #cant change it as it is primary key
        self._Department=dept #the dept the course belongs to
        self._Faculties=Faculties #the list of faculties handling the course
        self._CourseDetails=CourseDetails #a string of all details
        self.AVSummary=AVSumm #list of links using JSON type in MySQL
    
    def ViewCourse(self):#getter method, gets all or none
        pass#should return a dictionary with all values using key=CourseID

    def setter(self,di_of_values):
        if "CourseTitle" in di_of_values:
            self._CourseTitle=di_of_values["CourseTitle"]
        if "Department" in di_of_values:
            self._Department=di_of_values["Department"]
        if "Faculties" in di_of_values:
            self._Faculties=di_of_values["Faculties"]
        if "CourseDetails" in di_of_values:
            self._CourseDetails=di_of_values["CourseDetails"]
        if "AVS" in di_of_values:
            self.AVSummary=di_of_values["AVS"]
    
    def __repr__(self):
        return "\nStudent:\nID = {0}\n".format(self._CourseID)
        
        
        
