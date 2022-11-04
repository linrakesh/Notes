#program to create csv file using csv module
import csv
file = open('student.csv','w')

header =['admno','name','stream']
data =[[101,'rakesh','comm'],[102,'udit','human'],[103,'sumit','comm']]

writer = csv.writer(file,lineterminator='\n')

writer.writerow(header)
writer.writerows(data)

file.close()
print('CSV file Generated')
