"""
Sudoku Solver with Tkinter GUI

This code implements a Sudoku puzzle solver using a backtracking algorithm,
integrated with a graphical user interface (GUI) built with Tkinter.

Features:
---------
- 9x9 interactive Sudoku grid for user input
- Highlights 3x3 boxes with bold borders for better readability
- Pre-filled (user-entered) cells are highlighted in light gray
- Solved cells appear with a white background
- "Solve" button attempts to solve the current puzzle using backtracking
- "Reset" button clears the board
- Keyboard navigation with arrow keys and Enter key for fast input

Keyboard Controls:
------------------
- Arrow keys: Move between cells
- Enter: Move to the next cell (right, then next row)

How to Use:
-----------
1. Run the script to open the GUI window.
2. Enter known numbers into the Sudoku grid (1–9). Leave unknowns blank.
3. Click "Solve" to see the completed solution, if solvable.
4. Click "Reset" to clear the grid and start again.

Dependencies:
-------------
- Python 3.x
- Standard Tkinter module (comes with most Python installations)

Author: Minoo Sayyadpour
Date: 2025-07-13
"""
import tkinter as tk
from tkinter import messagebox

def valid_move(grid, row, col, number):
    """
        Check if placing a number at the specified position is valid according to Sudoku rules.

        Parameters:
        grid : list[list[int]]
            A 9x9 Sudoku grid represented as a list of lists.
        row : int
            Row index (0-based) where the number is to be placed.
        col : int
            Column index (0-based) where the number is to be placed.
        number : int
            The number (1–9) to be placed in the grid.
        --------------
        Returns:
        bool
            True if the number can be legally placed at the given position;
            False if it violates Sudoku constraints (row, column, or 3x3 box).
    """
    if number in grid[row]:
        return False
    for x in range(9):
        if grid[x][col] == number:
            return False
    corner_row = row - (row % 3)
    corner_col = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False
    return True

def solving(grid, row, col):
    """
       Recursively solves the given Sudoku grid using backtracking.

       This function attempts to fill the grid starting from the specified cell (row, col),
       moving left to right and top to bottom. If it finds a valid number for an empty cell,
       it proceeds to the next cell. If no valid number is found, it backtracks to try another possibility.

    -----------------
       Returns:
       bool
           True if the grid can be completely and validly filled;
           False if the puzzle has no solution from the current state.
    """
    if col == 9:
        if row == 8:
            return True
        else:
            row += 1
            col = 0
    if grid[row][col] > 0:
        return solving(grid, row, col + 1)
    for i in range(1, 10):
        if valid_move(grid, row, col, i):
            grid[row][col] = i
            if solving(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

class SudokuGUI:
    def __init__(self, root):
        """
            Initialize the Sudoku GUI.

            Sets up the 9x9 entry grid, configures buttons, enables keyboard navigation,
            and prepares internal state for tracking user input and solved cells.

            Parameters:
            -----------
            root : tk.Tk
                The main Tkinter root window.
        """
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.original_cells = [[False for _ in range(9)] for _ in range(9)]

        self.create_grid()
        self.selected_cell = (0, 0)  # for keyboard navigation

        solve_btn = tk.Button(root, text="Solve", command=self.solve_puzzle, font=('Arial', 14), bg='green', fg='white')
        solve_btn.grid(row=9, column=0, columnspan=5, sticky="nsew")

        reset_btn = tk.Button(root, text="Reset", command=self.reset_grid, font=('Arial', 14), bg='red', fg='white')
        reset_btn.grid(row=9, column=5, columnspan=4, sticky="nsew")

        self.bind_keys()

    def create_grid(self):
        """
        Create a 9x9 grid of Entry widgets for Sudoku input.

        Each cell is placed in the GUI with padding to visually highlight 3x3 boxes.
        Entry widgets are stored in a 2D list for easy access.
        """
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center', bg='white')
                entry.grid(row=i, column=j, padx=(2 if j % 3 == 0 else 1), pady=(2 if i % 3 == 0 else 1), ipady=5)
                entry.bind("<FocusIn>", lambda e, row=i, col=j: self.set_selected_cell(row, col))
                self.entries[i][j] = entry

    def bind_keys(self):
        """
        Bind arrow keys and Enter key for keyboard navigation.
        Allows the user to move between cells using the keyboard.
        """
        self.root.bind("<Up>", lambda e: self.move_selection(-1, 0))
        self.root.bind("<Down>", lambda e: self.move_selection(1, 0))
        self.root.bind("<Left>", lambda e: self.move_selection(0, -1))
        self.root.bind("<Right>", lambda e: self.move_selection(0, 1))
        self.root.bind("<Return>", lambda e: self.move_selection(0, 1))

    def set_selected_cell(self, row, col):
        """
            Update the currently selected cell coordinates.
            Called when an Entry gains focus to track keyboard navigation state.

            Parameters:
            -----------
            row : int
                Row index of the selected cell.
            col : int
                Column index of the selected cell.
        """
        self.selected_cell = (row, col)

    def move_selection(self, d_row, d_col):
        """
        Move the focus to a new cell based on row and column offsets.

        Ensures the new cell is within the grid bounds and sets focus there,
        updating the current selected cell for keyboard navigation.

        Parameters:
        -----------
        d_row : int
            Row offset to move (positive or negative).
        d_col : int
            Column offset to move (positive or negative).
        """
        row, col = self.selected_cell
        new_row = max(0, min(8, row + d_row))
        new_col = max(0, min(8, col + d_col))
        self.entries[new_row][new_col].focus_set()
        self.selected_cell = (new_row, new_col)

    def get_grid(self):
        """
           Retrieve the current Sudoku grid values from the GUI entries.

           Parses each Entry widget, converts valid digits (1–9) to integers,
           and marks cells as pre-filled or empty. Updates cell background colors accordingly.

           Returns:
           --------
           list[list[int]]
               A 9x9 grid of integers representing the current state of the Sudoku board,
               with 0 indicating empty cells.
        """
        grid = []
        self.original_cells = [[False for _ in range(9)] for _ in range(9)]
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit() and 1 <= int(val) <= 9:
                    row.append(int(val))
                    self.entries[i][j].config(bg='lightgray')
                    self.original_cells[i][j] = True
                else:
                    row.append(0)
                    self.entries[i][j].config(bg='white')
            grid.append(row)
        return grid

    def set_grid(self, grid):
        """
        Update the GUI entries to display the provided Sudoku grid.

        Fills only the cells that were not originally pre-filled by the user,
        and sets their background color to white.

        Parameters:
        -----------
        grid : list[list[int]]
            A 9x9 grid of integers representing the solved Sudoku board.
        """
        for i in range(9):
            for j in range(9):
                if not self.original_cells[i][j]:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(grid[i][j]))
                    self.entries[i][j].config(bg='white')

    def solve_puzzle(self):
        """
        Attempt to solve the Sudoku puzzle using the backtracking solver.

        Retrieves the current grid from the GUI, runs the solver,
        and updates the GUI with the solution if one exists.
        Displays an error message if no solution is found.
        """
        grid = self.get_grid()
        if solving(grid, 0, 0):
            self.set_grid(grid)
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists for the given puzzle.")

    def reset_grid(self):
        """
        Clear all entries in the Sudoku grid and reset cell backgrounds.

        returning the board to its initial empty state.
        """
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(bg='white')
        self.original_cells = [[False for _ in range(9)] for _ in range(9)]

root = tk.Tk()
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - 200
y = (screen_height // 2) - 200

root.geometry(f'412x430+{x}+{y}')
gui = SudokuGUI(root)
root.mainloop()
