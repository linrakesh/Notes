import mysql.connector as connector
conn = connector.connect(user='anu',password='pass1',host='127.0.0.1',database='school')
cursor = conn.cursor()
cursor.execute("insert into student values (111,'lakhanpal');")
conn.commit()
conn.close()
print('record added')