# program to find out intersection of two list elements

a = [10, 20, 60, 34, 23, 7, 23]
b = [34, 67, 78, 34, 89, 20, 10, 30, 45, 23]
inter = []
for x in a:
    if x in b:
        if x not in inter:
            inter.append(x)
print('Intersection of Two list is :', inter)
