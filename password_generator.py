from random import randint, shuffle

def simple_password_generator(number_of_characters=8):
 """Generates a simple password of random characters.

 This function creates a password of the specified length using random
 ASCII characters from the printable range (33 to 126).

 Args:
  number_of_characters: The desired length of the password. Defaults to 8.

 Returns:
  A string representing the generated password.
 """
 password_chars = [chr(randint(33, 126)) for _ in range(number_of_characters)]
 return ''.join(password_chars)


def password_generator(**kwargs):
 """Generates a password with customizable character types.

 This function allows you to specify the number of letters, numbers, and
 special characters to include in the password. The characters are then shuffled
 to create a random password.

 Args:
  **kwargs: Keyword arguments specifying the number of each character type:
   - 'number': The number of digits (0-9) to include.
   - 'letter': The number of letters (a-z or A-Z) to include.
   - 'special_character': The number of special characters (!@#$%^&* etc.)
    to include.

 Returns:
  A string representing the generated password.
 """
 password_chars = []

 if 'number' in kwargs:
  password_chars.extend([str(randint(0, 9)) for _ in range(kwargs['number'])])

 if 'letter' in kwargs:
  for _ in range(kwargs['letter']):
   if randint(0, 1) == 0:
    password_chars.append(chr(randint(65, 90))) # Uppercase
   else:
    password_chars.append(chr(randint(97, 122))) # Lowercase

 if 'special_character' in kwargs:
  for _ in range(kwargs['special_character']):
   rand_ascii = randint(33, 126)
   while chr(rand_ascii).isalnum(): # Ensure it's a special character
    rand_ascii = randint(33, 126)
   password_chars.append(chr(rand_ascii))

 shuffle(password_chars)
 return ''.join(password_chars)

print('############ complex password #############')
print(password_generator(letter=4, number=4, special_character=2))
print('############ simple password #############')
print(simple_password_generator(8))