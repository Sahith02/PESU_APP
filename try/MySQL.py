import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",database="mydatabase")
myc=mydb.cursor()
sql=("SELECT name_as_per_whatsapp from birthdays where DAY=%s and MONTH=%s")
myc.execute(sql,(curday,curmonth))#for %s ->curday
res=myc.fetchall()
mydb.close()

#TO create a table within it
#using the database/schema mydatabase
"""
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydatabase")

myc=mydb.cursor()
s='''Create table anniversaries
    (id int not null AUTO_INCREMENT PRIMARY KEY,
     DAY int,
     MONTH int check(MONTH>0 and MONTH<13),
     Name_as_per_whatsapp varchar(100));
     ALTER table birthdays AUTO_INCREMENT=1;'''

myc.execute(s,multi=True)#problems ho sakti hai idhar.multi hata dena->error aayega, waapas multi daal dena
myc.execute("SHOW TABLES")
"""

""" 
import mysql.connector
#To create a new schema i.e. DATABASE
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    #passwd='##############'
    )
myc=mydb.cursor()
myc.execute("CREATE schema mydatabase")
"""

"""
#inserting records within the table birthdays.
#using the database/schema mydatabase
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydatabase")
myc=mydb.cursor()
#multi=True when multiple queries in s
s='''Insert into anniversaries(DAY,MONTH,name_as_per_whatsapp) values
    (5,2,"Minaxi Bothra"),
    (5,2,"Sanjeev Bothra"),
    (23,11,"Rohit Giya"),
    (17,4,"Pankaj Giya"),
    (17,4,"Preeti Giya")
    ;'''
myc.execute(s)#doesn't push a tuple into the table
mydb.commit()#very important
"""