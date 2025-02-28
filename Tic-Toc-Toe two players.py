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
    # Check rows, columns, and diagonals
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

def tic_tac_toe():


    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row col): ").split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That cell is already occupied. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins! Congratulations!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()