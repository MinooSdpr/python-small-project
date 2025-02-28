import random

def roll_dice():
    """
    Simulates rolling two six-sided dice and returns their sum.

    Returns:
        int: The sum of the two dice rolls.
    """
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def cho_han_game(bet, guess):
    """
    Simulates a round of the Cho-han dice game.

    Parameters:
        bet (float): The amount of money the player bets.
        guess (str): The player's guess, either 'cho' (even) or 'han' (odd).

    Returns:
        tuple: A tuple containing the result of the game (win/loss), the sum of the dice, and the payout.
    """
    dice_sum = roll_dice()
    result = 'cho' if dice_sum % 2 == 0 else 'han'

    if guess == result:
        payout = bet * 1.9
        return 'win', dice_sum, payout
    else:
        return 'loss', dice_sum, 0

print("Welcome to Cho-han!")
print("Guess whether the sum of two dice will be even (cho) or odd (han).")

try:
    bet = float(input("Enter your bet amount: "))
    if bet <= 0:
        print("Bet must be a positive number.")
    else:
        guess = input("Enter your guess ('cho' for even, 'han' for odd): ").lower()
        if guess not in ['cho', 'han']:
            print("Invalid guess. Please enter 'cho' or 'han'.")
        else:
            outcome, dice_sum, payout = cho_han_game(bet, guess)

            print(f"\nThe sum of the dice is {dice_sum} ({'cho' if dice_sum % 2 == 0 else 'han'}).")
            if outcome == 'win':
                print(f"Congratulations! You won ${payout:.2f}!")
            else:
                print("Sorry, you lost. Better luck next time!")
except ValueError:
    print("Invalid input. Please enter a valid number.")