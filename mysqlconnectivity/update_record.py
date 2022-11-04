#program to update a record from mysql table- student
import mysql.connector as connector
conn = connector.connect(user='anu',password='pass1',host='127.0.0.1',database='school')
cursor = conn.cursor()

admno = input('Enter student admno whose name you want to update :')
name  = input('Enter new Name  :')

sql="update student set name ='{}' where admno ={}".format(name,admno)
#print(sql)
cursor.execute(sql)
conn.commit()
conn.close()
print('Record Successfully deleted')