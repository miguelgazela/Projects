# Check if Palindrome
# Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


def is_palindrome_alt(string):
    return string == string[::-1]

string = raw_input('String: ').lower()

if is_palindrome_alt(string):
    print string + ' is a palindrome'
else:
    print string + ' is not a palindrome'
