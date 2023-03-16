
def decode(text):
    decoded_text = ""

    for char in text:
        if char.isalpha():
            ascii_val = ord(char.lower()) - 13
            if ascii_val < ord("a"):
                ascii_val += 26
            decoded_text += chr(ascii_val).upper() if char.isupper() else chr(ascii_val)
        else:
            decoded_text += char
            

    return decoded_text