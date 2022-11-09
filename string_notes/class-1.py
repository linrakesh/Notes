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
