import bcrypt
def bcrypt_hash(message):
    encoded_message = message.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_message, salt)
    return hashed_password.decode()
   