# program to find out the sum of only integer elements available in a list
a = [10, 12.45, 'rakesh', 45, 'python fun', [10, 20], 5]
sum = 0
for x in a:
    if type(x) == int:
        sum = sum+x
print('Sum of integer elements :', sum)
