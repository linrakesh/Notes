# create a list of dictionary of 3 students
students = []
for x in range(3):
    admno = int(input('Enter admno :'))
    name = input('Enter student name :')
    stream = input('Enter student stream :')
    student = {'admno': admno, 'name': name, 'stream': stream}
    students.append(student)

print(students)
