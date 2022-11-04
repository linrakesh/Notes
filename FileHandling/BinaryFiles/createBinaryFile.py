#programs to save student information in a binary file
import pickle

file = open('student.dat','wb')
while True:
    name = input('Enter student name :')
    stream = input('Enter student stream :')
    fees = float(input('Enter Student Fees'))

    student = [name,stream,fees]
    
    pickle.dump(student,file)
    
    choice=input('Want to add more (y/n):').upper()
    if choice=='N':
        break

file.close()    
print('Record Added successfully')