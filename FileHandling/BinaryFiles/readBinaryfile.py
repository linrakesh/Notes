#programs to read student information from a binary file
import pickle

file = open('student.dat','rb')
while True:
    try:
        data = pickle.load(file)
        if (data[2]>200):
            print('Student Name :',data[0])
            print('Student Stream :',data[1])
            print('Student Fees :',data[2])
    except:
        break

file.close()
