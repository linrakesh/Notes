import mysql.connector as ridhima
conn=ridhima.connect(host="localhost",user="anu",password="pass1",database="school")
cursor = conn.cursor()

admno = input('Enter admission no :')
name  = input('Enter name :')

sql = "insert into student values({},'{}')".format(admno,name)
#print(sql)

cursor.execute(sql)
conn.commit()
conn.close()
print('Record Inserted ')