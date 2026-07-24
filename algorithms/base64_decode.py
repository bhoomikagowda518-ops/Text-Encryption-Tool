import base64
def base64_decode(encoded_message):
    base64_bytes=encoded_message.encode()
    decoded_bytes=base64.b64decode(base64_bytes)
    decoded_message=decoded_bytes.decode()
    return decoded_message


