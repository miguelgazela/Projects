# Count Words in a String
# Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

import string


def process_file(filename):
    hist = {}
    fin = open(filename)
    for line in fin:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation+string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

if __name__ == "__main__":
    hist = process_file("count_words.txt")
    print hist

