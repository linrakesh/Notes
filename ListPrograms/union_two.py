# program to find out union of two list elements

a = [10, 20, 60, 34, 23, 7, 23]
b = [34, 67, 78, 34, 89, 20, 10]
union = []
for x in a:
    if x not in union:
        union.append(x)

for x in b:
    if x not in union:
        union.append(x)
print(union)
