import string

def caesar_cipher(text, key, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher algorithm.

    Parameters:
        text (str): The input message to be encrypted or decrypted.
        key (int): The number of positions to shift each letter in the alphabet.
        mode (str): The mode of operation, either 'encrypt' or 'decrypt'.

    Returns:
        str: The transformed message after encryption or decryption.
    """
    alphabet = string.ascii_lowercase
    result = ''

    key = key % 26

    if mode == 'decrypt':
        key = -key

    for char in text:
        if char.lower() in alphabet:
            original_index = alphabet.find(char.lower())
            new_index = (original_index + key) % 26
            if char.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += char

    return result



text = input("Enter the message: ")
key = int(input("Enter the key (shift value): "))
mode = input("Choose mode ('encrypt' or 'decrypt'): ").lower()

if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
else:
    transformed_text = caesar_cipher(text, key, mode)
    print(f"Result: {transformed_text}")