import random

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Parameters:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Checks if the specified player has won the game.

    Parameters:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
        player (str): The player to check for a win ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    """
    Checks if the board is full (no empty cells left).

    Parameters:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all([cell != " " for row in board for cell in row])

def get_ai_move(board, ai_player, human_player):
    """
    Determines the AI's move using a simple rule-based strategy.

    Parameters:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
        ai_player (str): The AI's mark ('X' or 'O').
        human_player (str): The human player's mark ('X' or 'O').

    Returns:
        tuple: The row and column of the AI's move.
    """
    # Rule 1: Check if AI can win in the next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai_player
                if check_winner(board, ai_player):
                    board[i][j] = " " 
                    return i, j
                board[i][j] = " "

    # Rule 2: Check if human can win in the next move and block them
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = human_player
                if check_winner(board, human_player):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " " 

    # Rule 3: Take the center if it's available
    if board[1][1] == " ":
        return 1, 1

    # Rule 4: Take a corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for i, j in corners:
        if board[i][j] == " ":
            return i, j

    # Rule 5: Take any available edge
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(edges)
    for i, j in edges:
        if board[i][j] == " ":
            return i, j

def tic_tac_toe_with_ai():
    """
    Main function to play the Tic-Tac-Toe game with an AI opponent.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    ai_player = "O"
    current_player = human_player 

    print("Welcome to Tic-Tac-Toe with AI!")
    print_board(board)

    while True:
        if current_player == human_player:
            try:
                row, col = map(int, input("Enter your move (row col): ").split())
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Row and column must be between 0 and 2.")
                    continue
                if board[row][col] != " ":
                    print("That cell is already occupied. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
        else:
            print("AI is making a move...")
            row, col = get_ai_move(board, ai_player, human_player)

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            if current_player == human_player:
                print("Congratulations! You win!")
            else:
                print("AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = ai_player if current_player == human_player else human_player


tic_tac_toe_with_ai()