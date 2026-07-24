from algorithms.caesar_encrypt import caesar_encrypt
def rot13(message):
    return caesar_encrypt(message, 13)