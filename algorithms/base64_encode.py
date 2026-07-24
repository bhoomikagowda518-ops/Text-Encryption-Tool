import base64
def base64_encode(message):
    encoded_bytes = message.encode()
    base64_bytes = base64.b64encode(encoded_bytes)
    encoded_message = base64_bytes.decode()
    return encoded_message