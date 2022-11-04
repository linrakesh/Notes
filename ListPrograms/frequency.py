a = [12, 34, 213, 45, 67, 23, 45, 34, 56,
     232, 56, 23, 12, 3, 45, 67, 45, 67, 78]
value = []
count = []
for x in a:
    if x not in value:
        value.append(x)
        count.append(a.count(x))

for i in range(len(value)):
    print(value[i], 'appreaed ', count[i], 'times')
