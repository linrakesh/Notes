import random
words = ["rakesh", "ashok", "uditrajranjan",
         "nirmalbaba", 'suryansh', 'Bhavya']
word = words[random.randint(0, len(words)-1)]

# print(word)

guess = []

for x in range(len(word)):
    guess.append('-')

for x in guess:
    print(x, end=' ')

count = 1
while count < 5:
    char = input('\nEnter your char :')
    if word.count(char) >= 1:
        for x in range(len(word)):
            if word[x] == char:
                guess[x] = char
    else:
        count = count+1

    for x in guess:
        print(x, end=' ')

    if '-' not in guess and count < 5:
        print('\n\nHureey !!!! You Won this Game')
else:
    print('\n\nBOOOOOOOOOOO!!!! You Lost the Game')
