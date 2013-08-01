# Vigenere / Vernam / Ceasar Ciphers
# Functions for encrypting and decrypting data messages. Then send them to a friend.

import string


def shift_letter(letter, shift):
    if letter not in string.ascii_letters:
        return letter

    if letter in string.ascii_uppercase:
        start = ord('A')
    else:
        start = ord('a')

    return chr((ord(letter) - start + shift) % 26 + start) 


def ceasar_encrypt(message, shift):
    return ceasar_aux(message, shift)


def ceasar_decrypt(message, shift):
    return ceasar_aux(message, -shift)


def ceasar_aux(message, shift):
    res = ""
    for char in message:
        res += shift_letter(char, shift)
    return res


def vernam_encrypt(message):
    


def vernam_decrypt(message):
    pass


def vigenere_encrypt(message):
    pass


def vigenere_decrypt(message):
    pass


# testing ceasar cipher
encrypted_ceasar = ceasar_encrypt("AY", 3)
print encrypted_ceasar
print ceasar_decrypt(encrypted_ceasar, 3)

