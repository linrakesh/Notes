import mysql.connector as mysql
conn = mysql.connect(host='localhost', user='root',
                     password='', database='school')
cursor = conn.cursor()
sql = 'select * from student'
cursor.execute(sql)
records = cursor.fetchall()
for record in records:
    print(record)
conn.close()
