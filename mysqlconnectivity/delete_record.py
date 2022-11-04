#program to remove a record from mysql table- student
import mysql.connector as connector
conn = connector.connect(user='anu',password='pass1',host='127.0.0.1',database='school')
cursor = conn.cursor()

sql="delete from student where admno ="

admno = input('Enter student admno :')

sql =sql+" "+admno
#print(sql)
cursor.execute(sql)

conn.commit()

conn.close()

print('Record Successfully deleted')