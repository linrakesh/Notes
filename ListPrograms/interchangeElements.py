# program to interchange first element with second and third with fourth
# and so on
# example
#   a = [1, 25, 4, 6, 15, 9, 3, 7]
# result
#  a =  [25, 1, 6, 4, 9, 15, 7, 3]

a = [1, 25, 4, 6, 15, 9, 3, 7]
for x in range(0, len(a), 2):
    a[x], a[x+1] = a[x+1], a[x]

print(a)
