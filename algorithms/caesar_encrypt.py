def caesar_encrypt(message, key):
    encrypted = ""
    for letter in message:
        if letter.isupper():
            ascii_value = ord(letter)
            position = ascii_value - ord('A')
            new_position = position + key
            new_position = new_position % 26
            new_ascii = new_position + ord('A')
            encrypted_letter = chr(new_ascii)
            encrypted += encrypted_letter
        elif letter.islower():
            ascii_value = ord(letter)
            position = ascii_value - ord('a')
            new_position = position + key
            new_position = new_position % 26
            new_ascii = new_position + ord('a')
            encrypted_letter = chr(new_ascii)
            encrypted += encrypted_letter
        else: 
            encrypted += letter
    return encrypted
