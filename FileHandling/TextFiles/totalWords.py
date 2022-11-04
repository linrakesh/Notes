file = open('/home/lab/Desktop/Notes/FileHandling/TextFiles/sample.txt') # no mode means read mode
data = file.read() 
n = len(data.split())
print('Total words available in this file is ',n)
file.close()