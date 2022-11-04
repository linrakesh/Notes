a=[]
for  x in range(10):
    b = int(input('Enter any integer value '))
    a.append(b)

#print(a)
uniq=[]
for x in a:
    if x not in uniq:
        uniq.append(x)

print(uniq)
