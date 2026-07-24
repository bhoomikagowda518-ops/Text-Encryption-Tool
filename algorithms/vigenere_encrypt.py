def vigenere_encrypt(message, key):
    encrypted = ""
    key = key.upper()
    for i,letter in enumerate(message):
        key_letter = key[i % len(key)]
        if letter.isupper():
            letter_position = ord(letter) - ord('A')
            key_position = ord(key_letter) - ord('A')
            new_position = letter_position + key_position
            new_position%=26
            new_ascii=new_position+ord('A')
            encrypted_letter=chr(new_ascii)
            encrypted+=encrypted_letter
        elif letter.islower():
            letter_position = ord(letter) - ord('a')
            key_position = ord(key_letter) - ord('A')
            new_position = letter_position + key_position
            new_position%=26
            new_ascii=new_position+ord('a')
            encrypted_letter=chr(new_ascii)
            encrypted+=encrypted_letter
        else:
            encrypted+=letter
    return encrypted
