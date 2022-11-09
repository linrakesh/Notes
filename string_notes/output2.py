# find out the output of the following program segments

# prorgam- 1
str = "this is me rakesh and you are rakesh learning python"
data = str.split()
n = len(data)
# fill in the blank
print('Total Number of ........', n)


#program -2
# replace a word from a given string
str = "this is me rakesh and you are rakesh learning python"
str = str.replace('rakesh', 'Tajindar')
print(str)


#program -3
# remove a word from a given string
str = "this is me rakesh and you are rakesh learning python"
str = str.replace('rakesh', '')
print(str)


#program -4
# remove leading spaces
str = "    this is me"
str = str.lstrip()
print(str)

#program - 5
# remove trailing spaces
str = "This is me and this is             "
str = str.rstrip()
print(str)

#program - 6
# remove leading and trailing spaces
str = '  this is me and    '
str = str.strip()
print('Remove leading and trailing spaces :', str)

#program - 7
# change the case of each element ie lower to upper and upper to lower
str = 'hello Python students'
str = str.swapcase()
print(str)
