import mysql.connector as aa
conn = aa.connect(host='localhost', user='root',
                  password='', database='school')
cursor = conn.cursor()

admno = input('Enter admisssion No :')
name = input('Enter name :')
stream = input('Enter stream name :')

sql = "insert into student1 values({},'{}','{}')".format(admno, name, stream)
# print(sql)
cursor.execute(sql)
conn.commit()
conn.close()
print('Record inserted ....')
