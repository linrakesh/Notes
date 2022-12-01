a = [1, 2, 3, 4, 56, -1, 45, 5, 12, 34, 45]
b = [12, 34, 56, 67, 78, 78, 78, 78, 78, 34, 56]

for x, y in zip(a, b):
    print(x, y)

a = [x+1 for x in a if x % 2 == 0]
print(a)
