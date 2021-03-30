#student table: emailid,studname,SRN,Pgm,Address,PhoneNumber,Branch
#stucou table: mapping between student id and course id
import mysql.connector
class Student():
    def __init__(self,email,db_conn=None):
        if not(db_conn):
            db_conn=mysql.connector.connect(host = "localhost",port = 3306,user = "root",database = "pesuapp")
        cur=db_conn.cursor()
        query="SELECT studname,srn,pgm,`address`,phonenumber,branch FROM student WHERE emailid=%s"
        cur.execute(query,(email))
        res=cur.fetchone()
        cur.close()
        if res:
            self.email=email
            self.name,self.srn,self.pgm,self.address,self.phonenumber,self.branch=res
        
        