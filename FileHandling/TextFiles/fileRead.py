file = open('/home/lab/Desktop/Notes/FileHandling/TextFiles/sample.txt') # no mode means read mode
data = file.read() # read function reads whole file and return it as a string
# to it
print(type(data))
print(data)
file.close()