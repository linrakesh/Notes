# program -1

a = [1, 2, 4, 6, 10, 9, 3, 7]
for x in a:
    print(x, end=' # ')


# program-2
a = [1, 2, 4, 6, 10, 9, 3, 7]
dig = 0
for x in a:
    dig += x
print(dig)


# program-3
# find out the output of the following code
a = [1, 2, 4, 6, 10, 9, 3, 7]
dig = 0
for x in a:
    rem = x % 3
    if rem == 0:
        dig = dig+x
print(dig)


# program -4
a = [1, 2, 4, 6, 10, 9, 3, 7]
dig = 0
for x in a:
    rem = x % 3
    if rem == 0:
        dig = dig+x
else:
    print(dig)


# program -5
a = [1, 2, 4, 6, 10, 9, 3, 7]
result = a[0]
for x in range(1, len(a)):
    if result < a[x]:
        result = a[x]

print('Can you guess :', result)


# program -6
a = [1, 2, 4, 6, 10, 9, 3, 7]
data = 9
found = 0
for x in a:
    if x == data:
        found = 1
if(found == 1):
    # ............ suggest statement----
else:
    # ------------ suggest statement----
    print()


# program -7
a = [1, 25, 4, 6, 15, 9, 3, 7]
for x in a:
    rem = x % 10
    if rem == 5:
        print(x)
