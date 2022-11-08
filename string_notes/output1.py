# find out the output of the following python programs


# program-1
str = 'PythonFun'
for x in str:
    print(x, end='#')


#program - 2

string = "CBSE@Exam2023"
print(string[::-1])
if string == string[::-1]:
    print('Palindrome String')
else:
    print('Not a Palindrome String')


#program -3
str = "PythonFun2022"
for x in range(len(str)):
    if str[x].isupper():
        str[x] = str[x]-32
    elif str[x].isdigit():
        str[x] = str[x]+1
    else:
        str[x] = str[x]+32

print(str)


#program -4
str = "Python Fun 2022"
for x in range(len(str)):
    if str[x].isupper():
        str[x] = str[x]+32
    elif str[x].islower():
        str[x] = str[x]-32
    elif str[x].isdigit():
        str[x] = str[x]+1
    elif str[x].isspace():
        str[x] = '#'
    else:
        str[x] = str[x]+32

print(str)


# program -5
str = "PythonString-3.9"
for x in range(len(str)):
    if str[x].isupper():
        str[x] = str[x]+1
    else:
        if str[x].islower():
            str[x] = str[x]-1
        else:
            if str[x].decimal():
                str[x] = '#'
            else:
                if str.isnumeric():
                    str[x] = str[x]-1
print(str)


#prorgam -6
str = "Python For You"
for x in range(len(str)):
    if str[x].isupper():
        str[x] = str[x+1]
    else:
        if str[x].islower():
            str[x] = str[x]-1
        else:
            str[x] = '@'

print(str)
