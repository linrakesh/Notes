file = open('/home/lab/Desktop/Notes/FileHandling/TextFiles/sample.txt') 
data = file.read()
data = data.upper().split()  #called method chaining
n = data.count('THIS')
print('Total "this" words available in this file is ',n)
file.close()