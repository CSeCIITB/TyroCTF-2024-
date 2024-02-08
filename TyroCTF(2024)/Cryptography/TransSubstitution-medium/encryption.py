def substitution_cipher(text, key):
    encrypted_text = ''
    for char in text:
        if char in characters:
            char_index = characters.index(char)
            encrypted_char = characters[(char_index+key)%len(characters)]
            encrypted_text += encrypted_char
        else:
            # ignore any character which is not part of "characters" list and put it as it is.
            encrypted_text += char
    return encrypted_text

def transposition_cipher(text, key):
    encrypted_text = ''
    i=0
    while i < len(text):
        for index in key:
            encrypted_text += text[(i+index)%len(text)]
        i+=3
    return encrypted_text

def custom_encrypt(text, substitution_key, transposition_key):
    # Apply substitution cipher
    substitution_encrypted = substitution_cipher(text, substitution_key)

    # Apply transposition cipher
    transposition_encrypted = transposition_cipher(substitution_encrypted, transposition_key)

    return transposition_encrypted

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
flag = "REDACTED"
substitution_key = 0 # Some key in len(characters)
transposition_key = [0,1,2] # some combination of positions for 3 character blocks
encrypted_text = custom_encrypt(flag, substitution_key, transposition_key)
print("Encrypted:", encrypted_text)