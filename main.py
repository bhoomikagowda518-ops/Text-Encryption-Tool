from algorithms.caesar_encrypt import caesar_encrypt
from algorithms.caesar_decrypt import caesar_decrypt
from algorithms.rot13 import rot13
from algorithms.vigenere_encrypt import vigenere_encrypt
from algorithms.vigenere_decrypt import vigenere_decrypt
from algorithms.base64_encode import base64_encode
from algorithms.base64_decode import base64_decode
from algorithms.hex_encode import hex_encode
from algorithms.hex_decode import hex_decode
from algorithms.sha256 import sha256_hash
from algorithms.bcrypt_hash import bcrypt_hash
from algorithms.bcrypt_verify import bcrypt_verify
from algorithms.file_sha256 import file_sha256
from algorithms.fernet_encrypt import fernet_encrypt
from algorithms.fernet_decrypt import fernet_decrypt
from algorithms.file_encrypt import file_encrypt
from algorithms.file_decrypt import file_decrypt
from algorithms.aes_encrypt import aes_encrypt
from algorithms.aes_decrypt import aes_decrypt
from algorithms.aes_file_encrypt import aes_file_encrypt
from algorithms.aes_file_decrypt import aes_file_decrypt
from algorithms.rsa_encrypt import rsa_encrypt
from algorithms.rsa_decrypt import rsa_decrypt
from logger import log_error
while True:
    print("=================================")
    print("     TEXT ENCRYPTION TOOL")
    print("=================================")
    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. ROT13")
    print("4. Vigenère Encrypt")
    print("5. Vigenère Decrypt")
    print("6. Base64 Encode")
    print("7. Base64 Decode")
    print("8. Hex Encode")
    print("9. Hex Decode")
    print("10. SHA256 Hash")
    print("11. Bcrypt Hash")
    print("12. Bcrypt Verify")
    print("13. File SHA256 Hash")
    print("14. Fernet Encrypt")
    print("15. Fernet Decrypt")
    print("16. File Encrypt")
    print("17. File Decrypt")
    print("18. AES Encrypt")
    print("19. AES Decrypt")
    print("20. AES File Encrypt")
    print("21. AES File Decrypt")
    print("22. RSA Encrypt")
    print("23. RSA Decrypt")
    print("24. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    try:
        if choice == 1:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the key: "))
            result = caesar_encrypt(message, key)
            print("Encrypted Message:", result)
        elif choice == 2:
            message = input("Enter the message to decrypt: ")
            key = int(input("Enter the key: "))
            result = caesar_decrypt(message, key)
            print("Decrypted Message:", result)
        elif choice == 3:
            message = input("Enter the message to encrypt: ")
            result = rot13(message)
            print("Encrypted Message:", result)
        elif choice == 4:
            message = input("Enter the message to encrypt: ")
            key =input("Enter the key: ")
            result = vigenere_encrypt(message, key)
            print("encrypted Message:", result)
        elif choice == 5:
            message = input("Enter the message to decrypt: ")
            key =input("Enter the key: ")
            result = vigenere_decrypt(message, key)
            print("Decrypted Message:", result)
        elif choice == 6:
            message = input("Enter the message to encode: ")
            result = base64_encode(message)
            print("Encoded Message:", result)
        elif choice == 7:
            message = input("Enter the message to decode: ")
            result = base64_decode(message)
            print("Decoded Message:", result)
        elif choice == 8:
            message= input("Enter the message to encode: ")
            result = hex_encode(message)
            print("Encoded Message:", result)
        elif choice == 9:
            message= input("Enter the message to decode:")
            result = hex_decode(message)
            print("Decoded Message:", result)
        elif choice == 10:
            message = input("Enter the message to hash: ")
            result = sha256_hash(message)
            print("SHA256 Hash:", result)
        elif choice == 11:
            message = input("Enter the message to hash: ")
            result = bcrypt_hash(message)
            print("Bcrypt Hash:", result)
        elif choice == 12:
            password = input("Enter the password to verify: ")
            stored_hash = input("Enter the stored hash: ")
            result = bcrypt_verify(password, stored_hash)
            print("Bcrypt Verify:", result)
        elif choice == 13:
            try:
                file_path = input("Enter the file path: ")
                result = file_sha256(file_path)
                print("File SHA256 Hash:", result)
            except FileNotFoundError:
                print("File not found.")
        elif choice == 14:
            message = input("Enter the message to encrypt: ")
            result = fernet_encrypt(message)
            print("Encrypted Message:", result)
        elif choice == 15:
            encrypted_message = input("Enter the encrypted message: ")
            result = fernet_decrypt(encrypted_message)
            print("Decrypted Message:", result)
        elif choice == 16:
            try:
                file_path = input("Enter the file path: ")
                result = file_encrypt(file_path)
                print("File Encrypted:", result)
            except FileNotFoundError:
                print("File not found.")
        elif choice == 17:
            try:
                file_path = input("Enter the file path: ")
                result = file_decrypt(file_path)
                print("File Decrypted:", result)
            except FileNotFoundError:
                print("File not found.")
        elif choice == 18:
            message = input("Enter the message to encrypt: ")
            result = aes_encrypt(message)
            print("AES Encrypted:", result)
        elif choice == 19:
            encrypted_message = input("Enter the encrypted message: ")
            result = aes_decrypt(encrypted_message)
            print("AES Decrypted:", result)
        elif choice == 20:
            try:
                file_path = input("Enter file path: ")
                result = aes_file_encrypt(file_path)
                print("File Encrypted:", result)
            except FileNotFoundError:
                print("File not found.")
        elif choice == 21:
            try:
                file_path = input("Enter file path:")
                result = aes_file_decrypt(file_path)
                print("File Decrypt:", result)
            except FileNotFoundError:
                print("File not found.")
        elif choice == 22:
            message = input("Enter message to encrypt: ")
            result = rsa_encrypt(message)
            print("RSA Encrypted:", result)
        elif choice == 23:
            encrypted_message = input("Enter encrypted message: ")
            result = rsa_decrypt(encrypted_message)
            print("RSA Decrypted:", result)
        elif choice == 24:
            print("Exit")
            break
        else:
            print("Invalid Choice")
    except Exception as e:
        log_error(f"Error: {e}")
        print("Something went wrong. Please check your input.")