def find_next_empty(puzzle):
    # Finds next empty space
    # Return row, column to represent space (returns None if there are no spaces available)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None 

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