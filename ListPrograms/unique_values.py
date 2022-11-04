a = [12, 34, 213, 45, 67, 23, 45, 34, 56,
     232, 56, 23, 12, 3, 45, 67, 45, 67, 78]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)
