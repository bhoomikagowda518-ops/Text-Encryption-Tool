import hashlib
def sha256_hash(message):
    encoded_message = message.encode()
    hash_object = hashlib.sha256(encoded_message)
    real_hash = hash_object.hexdigest()
    return real_hash