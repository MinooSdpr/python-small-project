def caesar_encryption(number, text):
  """Encrypts a string using Caesar cipher, shifting all characters.

  This function shifts each character in the input text by the specified
  number, wrapping around the ASCII table. It does not handle alphabetic
  characters differently.

  Args:
    number (int): The shift value for the cipher.
    text (str): The text to encrypt.

  Returns:
    str: The encrypted text.
  """
  output = ''
  for i in text:
    output += chr(ord(i) + number)
  return output

def caesar_decryption(number, enc_text):
  """Decrypts a string encrypted with Caesar cipher, shifting all characters.

  This function shifts each character in the encrypted text back by the
  specified number, wrapping around the ASCII table. It does not handle
  alphabetic characters differently.

  Args:
    number (int): The shift value for the cipher.
    enc_text (str): The encrypted text.

  Returns:
    str: The decrypted text.
  """
  output = ''
  for i in enc_text:
    output += chr(ord(i) - number)
  return output

def caesar_encryption_only_alpha(number, text):
 """Encrypts a string using Caesar cipher, only for alphabet characters.

 Args:
  number (int): The shift value for the cipher.
  text (str): The text to encrypt.

 Returns:
  str: The encrypted text.
 """
 output = ''
 for i in text:
  if i.isalpha():
   if i.isupper():
    output += chr(((ord(i) + number - 65) % 26) + 65) 
   else:
    output += chr(((ord(i) + number - 97) % 26) + 97)
  else:
   output += i
 return output

def caesar_decryption_only_alpha(number, text):
 """Decrypts a string encrypted with Caesar cipher, only for alphabet characters.

 Args:
  number (int): The shift value for the cipher.
  text (str): The encrypted text.

 Returns:
  str: The decrypted text.
 """
 output = ''
 for i in text:
  if i.isalpha(): 
   if i.isupper(): 
    output += chr(((ord(i) - number - 65) % 26) + 65)
   else: 
    output += chr(((ord(i) - number - 97) % 26) + 97)
  else: 
   output += i
 return output



while True:
  try:
    choice = int(input('Enter your choice:\n1: Encrypt\n2: Decrypt\n3: Exit\n'))
    match choice:
      case 1:
        text = input('Enter your simple text: ')
        encrypt_number = int(input('Enter the encrypt code: '))
        print(caesar_encryption_only_alpha(encrypt_number,text))
      case 2:
        text = input('Enter your encrypted text: ')
        decrypt_number = int(input('Enter the decrypt code: '))
        print(caesar_decryption_only_alpha(decrypt_number,text))
      case 3:
        break
  except:
    print(chr(27) + "[2J")
    print('You enter a wrong input. Try again.')
