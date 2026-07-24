def caesar_decrypt(message,key):
    decrypted = ""
    for letter in message:
         if letter.isupper():
            ascii_value = ord(letter)
            position = ascii_value - ord('A')
            new_position = position - key
            new_position = new_position % 26
            new_ascii = new_position + ord('A')
            decrypted_letter = chr(new_ascii)
            decrypted += decrypted_letter
         elif letter.islower():
              ascii_value = ord(letter)
              position = ascii_value - ord('a')
              new_position = position - key
              new_position = new_position % 26
              new_ascii = new_position + ord('a')
              decrypted_letter = chr(new_ascii)
              decrypted += decrypted_letter
         else:
             decrypted += letter
    return decrypted