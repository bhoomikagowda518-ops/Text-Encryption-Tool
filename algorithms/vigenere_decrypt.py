def vigenere_decrypt(message, key):
    decrypted = ""
    key = key.upper()
    for i,letter in enumerate(message):
        key_letter = key[i % len(key)]
        if letter.isupper():
            letter_position = ord(letter) - ord('A')
            key_position = ord(key_letter) - ord('A')
            new_position = letter_position - key_position
            new_position%=26
            new_ascii=new_position+ord('A')
            decrypted_letter=chr(new_ascii)
            decrypted+=decrypted_letter
        elif letter.islower():
            letter_position = ord(letter) - ord('a')
            key_position = ord(key_letter) - ord('A')
            new_position = letter_position - key_position
            new_position%=26
            new_ascii=new_position+ord('a')
            decrypted_letter=chr(new_ascii)
            decrypted+=decrypted_letter
        else:
            decrypted+=letter
    return decrypted