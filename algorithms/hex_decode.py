def hex_decode(message):
    decoded = ""
    parts = message.split(" ")
    for value in parts:
        decimal_value=int(value,16)
        decoded_letter=chr(decimal_value)
        decoded +=decoded_letter
    return decoded