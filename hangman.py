import random
words =["rakesh","ashok","uditrajranjan","nirmalbaba"]
word = words[random.randint(0,len(words)-1)]

print(word)
guess=[]
for x in range(len(word)):
        guess.append('-')

for x in guess:
    print(x, end= ' ')

count=1
while True:
    char = input('Enter your char :')
    if word.count(char)>=1:
        for x in range(len(word)):
            if word[x]==char:
                guess[x]=char
        
    for x in guess:
        print(x,end= ' ')
    count=count+1
    if count>15:
        break



