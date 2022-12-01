import mysql.connector as aa
conn = aa.connect(host='localhost', user='root',
                  password='', database='school')
cursor = conn.cursor()

admno = input('Enter admisssion No :')
sql = "delete from student1 where admno = {}".format(admno)
# print(sql)
cursor.execute(sql)
conn.commit()
conn.close()
print('Record Delete ....')
