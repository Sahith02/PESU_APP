#student table: emailID,Name,SRN,Program,Address...
#create a table STUCOU using student ID and course IDS

class Student():
    def __init__(self,email):
        #calls the database based on the email and brings in the below values
        self.email=email
        self.Name=Name
        self.SRN=SRN #primary key
        self._Program=pgm
        self._Address=address
        self._PhoneNumber=phone
        self._Branch=branch
        self.CoursesEnrolled=[] #list of course ID's which we get from the STUCOU table
    
    def seedetails(self):#GETTER method you would want to get all the private values of program,...,_branch]
        pass

    def editdetails(self):#SETTER method
        pass

    def CheckEventNotification(self):
        pass

    def CheckCourses(self):
        pass

    def GiveCourseFeedback(self):
        pass

    def __repr__(self):
    	return "\nStudent:\nID = {0}\n".format(self.SRN)
