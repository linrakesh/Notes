# create a dictionary of 3 students ( dictionary of dictionary)
students = {}
for x in range(3):
    admno = int(input('Enter admno :'))
    name = input('Enter student name :')
    stream = input('Enter student stream :')
    student = {'name': name, 'stream': stream}
    students[admno] = student

for record in students:
    print(students[record]['name'])
    print(students[record]['stream'])
