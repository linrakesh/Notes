string = "this is me and i am trying to learn python by examples"
freq = {}
for x in string:
    if x not in freq:
        freq[x] = string.count(x)

print(freq)
