#programs to read student information from a binary file
import pickle

file = open('student.dat','rb')
data = pickle.load(file)

print('Student Name :',data['name'])
print('Student Stream :',data['stream'])
print('Student Fees :',data['fees'])

file.close()