import hashlib
from logger import log_info
def file_sha256(file_path):
    with open(file_path, "rb") as file:
      file_bytes = file.read()
    hash_object = hashlib.sha256(file_bytes)
    hash_value = hash_object.hexdigest()
    log_info("File SHA256 Hash Generated")
    return hash_value