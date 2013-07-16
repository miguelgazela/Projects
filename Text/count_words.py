# Count Words in a String
# Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

fin = open("count_words.txt")

words = []
counter = []

for line in fin:
    line = line.strip()
    line_words = line.split()

    for word in line_words:
        if word in words:
            i = words.index(word)
            counter[i] += 1
        else:
            words.append(word)
            counter.append(1)

res = []
for i in range(len(words)):
    res.append([words[i], counter[i]])

print res

