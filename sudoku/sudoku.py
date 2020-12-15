def find_next_empty(puzzle):
    # Finds next empty space
    # Return row, column to represent space (returns None if there are no spaces available)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None 

def is_valid(puzzle, guess, row, col):
    # Determines if the guess is valid or not
    # Returns True if valid, else returns False
    row_values = puzzle[row]
    # If the user's guess is already a number in that row, return False
    if guess in row_values:
        return False

    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    # Find where the individual 3x3 square matrix begins
    # iterate over the 3 values in each row/column
    starting_row = (row // 3) * 3
    starting_column = (col // 3) * 3

    for r in range(starting_row, starting_row + 3):
        for c in range(starting_column, starting_column + 3):
            if puzzle[r][c] == guess:
                return False

    return True # Returns True if all validation checks pass

def solve_sudoku(puzzle):
    # Use backtracking method to solve sudoku puzzle
    # Returns True if a solution exists or False if it doesn't
    # If a solution does exist, the puzzle is manipulated to be the solution

    # Pick a spot on the board to make an initial guess
    row, column = find_next_empty(puzzle) # Helper function

    # Validate if the inital guess is a valid input
    if row is None:
        return True

    # If there's a spot for a number guess, make a guess between 1 and 9
    for guess in range(1, 10):
        # Check if this guess is valid
        if is_valid(puzzle, guess, row, column): # Another helper function
            pass