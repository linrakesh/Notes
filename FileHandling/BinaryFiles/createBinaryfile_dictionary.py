#programs to save student information in a binary file
import pickle

file = open('student.dat','wb')

name = input('Enter student name :')
stream = input('Enter student stream :')
fees = float(input('Enter Student Fees'))

student = {'name':name,'stream':stream,'fees':fees}

pickle.dump(student,file)
print('Record Added successfully')