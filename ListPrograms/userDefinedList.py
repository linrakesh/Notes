# program to generate user defind list
n = int(input('Enter total number of elements you want in list :'))
a = []  # create blank list
for i in range(n):
    x = int(input('Enter list element :'))
    a.append(x)

# finally print your list
print('Your list is :', end=' ')
print(a)
