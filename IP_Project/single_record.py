import mysql.connector as aa
conn = aa.connect(host='localhost', user='root',
                  password='', database='school')
cursor = conn.cursor()
admno = input('Enter admission NO :')
sql = "select * from student1 where admno ={}".format(admno)
# print(sql)
cursor.execute(sql)
result = cursor.fetchone()
print(result)
conn.close()
