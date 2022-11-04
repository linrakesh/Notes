#program to create csv file using csv module
import csv
file = open('student.csv','r')

data = csv.reader(file)
for row in data:
     print(row)


file.close()
