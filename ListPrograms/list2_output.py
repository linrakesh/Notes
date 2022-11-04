# find out the output of the following code
# based on single position accessing and slicing
a = [10, 20, 30, 450, 56, 78, 34, 7]
print(a)
print(a[2:5])
print(a[:5])
print(a[1:7:2])
a[2:5] = 100, 200, 300
print(a)
a[6] = 1000
print(a[7])
print(a[-7:-4])
print(a[::-1])
print(a[-7:-1:2])
print(a[-7: -3: -1])
