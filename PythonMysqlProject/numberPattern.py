n = int(input('Enter any no :'))
for x in range(n+1):
    for z in range(n-1-x,-1,-1):
        print(' ',end =' ')
    for y in range(1,x+1):
        print(y,end =' ')
    for w in range(x-1,0,-1):
        print(w,end=' ')
    print()

for x in range(n-1,0,-1):
    for z in range(n-1-x,-1,-1):
        print(' ',end =' ')
    for y in range(1,x+1):
        print(y,end =' ')
    for w in range(x-1,0,-1):
        print(w,end=' ')
    print()