#program to fetch a single record from mysql table- student
import mysql.connector as connector
conn = connector.connect(user='anu',password='pass1',host='127.0.0.1',database='school')
cursor = conn.cursor()

sql ="select * from student"

cursor.execute(sql)
result = cursor.fetchall()

for row in result:
    print(row)

conn.close()

