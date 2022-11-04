import mysql.connector as connector
conn = connector.connect(user='anu',password='pass1',host='127.0.0.1',database='school')
cursor = conn.cursor()

sql="insert into student(admno,name) values ("

admno = input('Enter student admno :')
name  = input('Enter student name :')
sql =sql+" "+admno+",'"+name+ "')"
#print(sql)
cursor.execute(sql)
conn.commit()
conn.close()
print('record added')