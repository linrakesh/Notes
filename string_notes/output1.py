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
string = "PythonFun2022"
str1 = ''
for x in range(len(string)):
    if string[x].isupper():
        str1 += chr(ord(string[x])+32)
    elif string[x].isdigit():
        str1 += chr(ord(string[x])+1)
    else:
        str1 += chr(ord(string[x])-32)
print(str1)


#program -4
string = "Python Fun 2022"
str1 = ''
for x in range(len(string)):
    if string[x].isupper():
        str1 += chr(ord(string[x])+32)
    elif string[x].islower():
        str1 += chr(ord(string[x])-32)
    elif string[x].isdigit():
        str1 += chr(ord(string[x])+1)
    elif string[x].isspace():
        str1 += '#'

print(str1)


# program -5
str1 = "PythonString-3.9"
str2 = ''
for x in range(len(str1)):
    if str1[x].isupper():
        str2 += chr(ord(str1[x])+1)
    else:
        if str1[x].islower():
            str2 += chr(ord(str1[x])-1)
        else:
            if str1[x].isdecimal():
                str2 += '#'
            else:
                if str1.isnumeric():
                    str2 += chr(ord(str[x])-1)
print(str2)


#prorgam -6
str1 = "Python For You"
str2 = ''
for x in range(len(str1)):
    if str1[x].isupper():
        str2 += str1[x+1]
    else:
        if str1[x].islower():
            str2 += chr(ord(str1[x])-1)
        else:
            str2 += '@'

print(str2)
