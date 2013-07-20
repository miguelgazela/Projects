def read_words(filename):
    res = []
    try:
        fin = open(filename)
        for line in fin:
            word = line.strip()
            res.append((word, False))
        fin.close()
        return res
    except:
        print "Something went wrong with file operation"


def get_unused_random_word(words):
    pass


if __name__ == "__main__":
    words = read_words("words.txt")
    print words 