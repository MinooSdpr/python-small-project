"""
This script simulates a simple game where the player "pushes a button" to generate a random combination of symbols.
The symbols represent different outcomes that affect the player's bonus and tickets.

Game Rules:
1. Each round, the player gets a random combination of 3 symbols:
   - '💰': Represents gold. Each gold symbol adds 20 to the bonus.
   - '❔': Represents a question mark. Each question mark earns the player 1 additional ticket.
   - '☠️': Represents a skeleton. If all 3 symbols are skeletons, the bonus is reset to 0, and the game ends immediately.

2. Special Win Condition:
   - If all 3 symbols are gold ('💰'), the player wins an additional 1,000,000 bonus.

3. Gameplay:
   - The player starts with 1 ticket.
   - Each round consumes 1 ticket.
   - The player can choose to continue playing if they have tickets remaining.
   - The game ends when:
     - The player runs out of tickets.
     - The player chooses to stop.
     - The result is ['☠️', '☠️', '☠️'] (bonus is reset to 0, and the game ends immediately).

4. Output:
   - At the end of the game, the player's total bonus is displayed.
"""

from random import choices

def push_button():
    """
    Simulates pushing a button and returns a random combination of symbols.

    Returns:
        list: A list of 3 symbols randomly chosen from ['❔', '☠️', '💰'].
    """
    situations = ['❔', '☠️', '💰']
    return choices(situations, k=3)

def calculate_bonus(chance, bonus):
    """
    Calculates the bonus based on the symbols in the current chance.

    Args:
        chance (list): A list of 3 symbols representing the current result.
        bonus (int): The current bonus amount.

    Returns:
        tuple: A tuple containing the updated bonus, the number of tickets earned, and a flag indicating if the game should end.
    """
    gold_count = chance.count('💰')
    question_count = chance.count('❔')
    skeleton_count = chance.count('☠️')

    bonus += gold_count * 20

    if skeleton_count == 3:
        bonus = 0
        return bonus, question_count, True  # End the game
    elif gold_count == 3:
        bonus += 1_000_000

    return bonus, question_count, False  # Continue the game

def main():
    """
    Main function to simulate the game.
    """
    bonus = 0
    ticket = 1

    while ticket > 0:
        ticket -= 1
        chance = push_button()
        print(chance)

        bonus, question_count, end_game = calculate_bonus(chance, bonus)
        ticket += question_count

        if end_game:
            print("Game Over! You got ['☠️', '☠️', '☠️']. Bonus reset to 0.")
            break

        if ticket > 0:
            continue_or_exit = input('Do you want to continue? [y/n]: ').strip().lower()
            if continue_or_exit == 'n':
                break

    print(f'You win {bonus}$')

main()