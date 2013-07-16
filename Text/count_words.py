# Count Words in a String
# Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

fin = open("count_words.txt")

words = {}

for line in fin:
    line = line.strip()
    line_words = line.split()

    for word in line_words:
        words[word] = words.get(word, 0) + 1

print words

