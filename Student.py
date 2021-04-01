#student table: emailid,studname,srn,pgm,address,phonenumber,branch
#stucou table: mapping between student id and course id
#stucou table=courseid,studentid

import mysql.connector
from Course import Course#used to get the courses

class Student():
    def __init__(self,db_conn,email):
        # if not(db_conn):
        #     db_conn=mysql.connector.connect(host = "localhost",port = 3306,user = "root",database = "pesuapp")
        cur=db_conn.cursor()
        query="SELECT studname,srn,pgm,`address`,phonenumber,branch FROM student WHERE emailid=%s"
        cur.execute(query,(email,))
        res=cur.fetchone()
        if res:
            self.email=email
            self.name,self.srn,self.pgm,self.address,self.phonenumber,self.branch=res
    
    def ViewCourses(self,db_conn):
        cur=db_conn.cursor()
        query="SELECT courseid FROM stucou WHERE studentid=%s"
        cur.execute(query,(self.srn,))
        res=cur.fetchall()
        cur.close()
        courses=[]
        if res:
            courses=[Course(db_conn,x[0]) for x in res]
        return courses

    def EditDetails(self,db_conn,address="",phonenumber=""):
        if address or phonenumber:
            cur=db_conn.cursor()
            if address:
                query="UPDATE student SET `address`=%s WHERE srn=%s"
                cur.execute(query,(address,self.srn,))
                db_conn.commit()
            if phonenumber:
                query="UPDATE student SET phonenumber=%s WHERE srn=%s"
                cur.execute(query,(phonenumber,self.srn,))
                db_conn.commit()
            cur.close()


    def ViewAnnouncements(self,db_conn):
        pass
    
    def GiveCourseFeedback(self,db_conn):
        pass

    def __repr__(self):
        return f"\nStudent\nName:{self.name}\nID:{self.srn}\n"
        