import random

# Create a board object
class Board:
    def __init__(self, dimension_size, num_bombs):
        self.dimension_size = dimension_size
        self.num_bombs = num_bombs

        # Generate game board
        self.board = self.make_new_board()

        # Keeps track of which locations have been discovered
        self.dug = set()

    def make_new_board(self):
        # Construct the board based on dimension size and number of bombs

        # Generate new board
        board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]

        # Plant bombs on game board
        planted_bombs = 0
        while planted_bombs < self.num_bombs:
            bomb_location = random.randint(0, self.dimension_size**2 - 1)
            row = bomb_location // self.dimension_size
            column = bomb_location % self.dimension_size

            # '*' represents a bomb in this version of minesweeper
            if board[row][column] == '*':
                # If there's a bomb, then number of planted bombs will not increment
                


# Play Minesweeper
def play(dimension_size=10, num_bombs=10):
    # Create the game board

    # Ask for user input

    # If the location the user picked is where a bomb is placed, game's over

    # If the location is not where a bomb is, use recursive function to dig in other spots 
    # until each square is next to a bomb

    # Repeat steps 2, 3, and 4 until there are no more bombs

    pass


