def hex_encode(message):
    encoded = ""
    for letter in message:
        ascii_value = ord(letter)
        hex_value = hex(ascii_value)
        hex_value = hex_value[2:]
        encoded += hex_value + " "
    encoded = encoded[:-1]
    return encoded