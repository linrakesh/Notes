#program to fetch a multiple records from mysql table- student

import mysql.connector as connector
conn = connector.connect(user='anu',password='pass1',host='127.0.0.1',database='school')
cursor = conn.cursor()

sql="select * from student"
#print(sql)
cursor.execute(sql)
result= cursor.fetchall()   #fetchall is used to fetch all the records
print(result)
conn.close()