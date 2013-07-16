# Pig Latin
# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound is
# transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
# Read Wikipedia for more information on rules.

vowels = 'aeiou'
pig = 'ay'
res = ''

string = raw_input("String: ")

words = string.split(' ') # doesn't work with punctuation

for word in words:
    if word[0] in vowels:
        res += word + "w" + pig + ' ' 
    else:
        res += word[1:] + word[0] + pig + ' '

print res
