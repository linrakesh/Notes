a=[]
for  x in range(10):
    b = int(input('Enter any integer value '))
    a.append(b)

#print(a)

uniq=[]
freq=[]
for x in a:
    if x not in uniq:
        uniq.append(x)
        freq.append(a.count(x))

print(uniq)
print(freq)