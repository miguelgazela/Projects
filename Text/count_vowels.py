# Count Vowels
# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

vowels = ['a', 'e', 'i', 'o', 'u']
counter = [0, 0, 0, 0, 0]


def count_vowels(string):
    for i in range(0, 5):
        counter[i] = string.count(vowels[i])

count_vowels(raw_input('String: '))

for i in range(0, 5):
    print vowels[i] + ": " + str(counter[i])
