str = "PythonFun2022"
for x in range(len(str)):
    if str[x].isupper():
        str[x] = str[x]- 32
    elif str[x].isdigit():
        str[x] = str[x]+1
    else:
        str[x] = str[x]+32

print(str)