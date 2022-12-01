import mysql.connector as aa
conn = aa.connect(host='localhost', user='root',
                  password='', database='school')
cursor = conn.cursor()

admno = input('Enter admisssion No :')
name = input('Enter new name :')
stream = input('Enter new stream :')

sql = "update student1 set name = '{}', stream = '{}' where admno = {}".format(
    name, stream, admno)
# print(sql)
cursor.execute(sql)
conn.commit()
conn.close()
print('Record updated ....')
