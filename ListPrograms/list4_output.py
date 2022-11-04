#program -1
a = [10, 20, 30, 40, 45]
a.append(100)
a.insert(2, 200)
print(a)


# program-2
a = [10, 20, 30, 40, 45]
a.insert(1, [200, 300])
a.extend([300, 400])
print(a)

# program-3
a = [10, 20, 30, 40, 45]
a.remove(20)
a.pop()
a.append(200)
print(a)

#program -4
a = [10, 20, 30, 40, 45]
b = a
b.insert(2, 999)
a.insert(3, 500)
print(a)
print(b)

# program-5
a = [10, 20, 30, 40, 45]
b = a.copy()
a.append(2000)
print(a)
print(b)


#program -6
a = [10, 20, 30, 40, 45]
b = [323, 45, 76, 89, 45, 67]
a.sort(reverse=True)
b.sort(reverse=False)
print(a)
print(b)

#program -7
a = [10, 20, 30, 40]
b = a
a[2] = 100
print(a)
print(b)
