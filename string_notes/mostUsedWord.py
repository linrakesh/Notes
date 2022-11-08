# program to find out frequency of each word

str = "Today, with more than half of the world’s population online, it’s \
      critical for any business to adopt a digital marketing strategy. These tools \
      can increase your sales , generate leads, and earn a significant profit if done correctly. Read on to learn more about five digital marketing tools for your small business. \
      You might be surprised to find out how effective these tools can be.\
      Listed below are some of the most useful ones"
data = str.split()
uniq = []
freq = []
for word in data:
    if word not in uniq:
        uniq.append(word)
        freq.append(data.count(word))

# display results
for x in range(len(uniq)):
    print(uniq[x], 'appeared ', freq[x], 'times')


# most used word in this string
index = max(freq)
print('Most used word is "', uniq[index], '" appeared', index, ' times')
