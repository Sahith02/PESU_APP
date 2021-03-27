
from User import User

class Student(User):
    def __init__(self,Name,pwd,emailid,SRN,pgm,address,phone,branch,courses):
        super().__init__(Name,pwd,emailid)
        self.SRN=SRN
        self._Program=pgm
        self._Address=address
        self._PhoneNumber=phone
        self._Branch=branch
        self.CoursesEnrolled=[]
    
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





'''
class A:
    _ne=5
    def __init__(self):
        self._name="sasas"
obj=A()
print(A._name) # error: type object 'A' has no attribute '_name'
'''

