# find out the output of the following program segments

# prorgam- 1
str = "Today, with more than half of the world’s population online, it’s \
      critical for any business to adopt a digital marketing strategy. These tools \
      can increase your sales , generate leads, and earn a significant profit if done correctly. Read on to learn more about five digital marketing tools for your small business. \
      You might be surprised to find out how effective these tools can be.\
      Listed below are some of the most useful ones"
data = str.split()
n = len(data)
# fill in the blank
print('Total Number of ...............', n)


#program -2
# replace a word from a given string
str = str.replace('sales', 'BAADSHAH')
print(str)

#program -3
# remove a word from a given string
str = str.replace('BAADSHAH', '')
print(str)

#program -4
# remove leading spaces
str = "    this is me"
str = str.lstrip()
print(str)

#program - 5
# remove trailing spaces
str = "This is me and this is example of trailing spaces            "
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
