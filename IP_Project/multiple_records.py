import mysql.connector as aa
conn = aa.connect(host='localhost', user='root',
                  password='', database='school')
cursor = conn.cursor()
#admno = input('Enter admission NO :')
sql = "select * from student1"
# print(sql)
cursor.execute(sql)
result = cursor.fetchall()
for record in result:
    print(record)
conn.close()
