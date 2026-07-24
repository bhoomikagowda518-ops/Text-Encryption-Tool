import bcrypt
def bcrypt_verify(password, stored_hash):
    password_bytes = password.encode()
    stored_hash_bytes = stored_hash.encode()
    bcrypt.checkpw(
    password_bytes,
    stored_hash_bytes
)
    return bcrypt.checkpw(password_bytes, stored_hash_bytes)