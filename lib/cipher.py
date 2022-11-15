# Cipher: ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']
# String: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
# Letter: T

# Index of T is 4
# Add 65 + 4 = 69
# Call Char(69) = 'E'

def encode(text, key):
    cipher = make_cipher(key)
    # print(cipher)
    ciphertext_chars = []
    # print('Iterating over letters in text')
    # print(cipher)
    for i in text:
        # print(f'Letter ({i})')
        # print(f'Cipher index: {cipher.index(i)}')
        ciphered_char = chr(65 + cipher.index(i)) #Expects 'a' to be here
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        # print(f"Letter i is {i}'")
        # print(f"Letter ord(i) is {ord(i)}")
        # print(f"Letter (65 - ord(i)) is {(65 - ord(i))}")
        # print(f"Letter cipher[65 - ord(i)] is {cipher[65 - ord(i)]}")
        plain_char = cipher[ord(i) - 65] # Minus was suspicious, flipped other way round
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)] #Not a Alphabet
    # print('Key')
    # print(list(key))
    # print('Alphabet')
    # print(alphabet)
    cipher_with_duplicates = list(key) + alphabet
    # print('With duplicates:')
    # print(cipher_with_duplicates)

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    # print('Without duplicates:')
    # print(cipher)


    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")