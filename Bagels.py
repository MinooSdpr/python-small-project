"""
In Bagels, a deductive logic game, you must guess a secret three-digit number
based on clues. The game offers one of the following hints in response to your guess:
“Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess 
has a correctdigit in the correct place, and “Bagels” if your guess has no correct digits.
 You have 10 tries to guess the secret number.
"""
from random import randint

def get_clues(secret_number,guess):
    """Returns a string of clues based on the guess."""
    secret_number_str = str(secret_number)
    guess_str = str(guess)
    response = 'Bagels'
    for i in range(0,3):
        if secret_number_str[i]==guess_str[i]:
            response='Fermi'
            break
        if guess_str[i] in secret_number_str:
            response='Pico'
    return response

secret_number = randint(100,999)
tries = 10

while tries>0:
    guess = int(input('Guess the secret three digit number:'))
    if secret_number==guess:
        print('You guess the number!')
        break
    print(get_clues(secret_number,guess))
    tries-=1
    if tries == 0:
        print("You ran out of tries. The secret number was:", secret_number)