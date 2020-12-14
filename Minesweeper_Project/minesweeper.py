import random, re

# Create a board object
class Board:
    def __init__(self, dimension_size, num_bombs):
        self.dimension_size = dimension_size
        self.num_bombs = num_bombs

        # Generate game board
        self.board = self.make_new_board()
        self.assign_values_to_board()

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
                continue
            # Else, plant a bomb, increment the bombs_planted counter, and then return the game board
            board[row][column] = '*'
            planted_bombs += 1
        return board
    
    def assign_values_to_board(self):
        """
        Once the bombs have been planted, a number between 0-8 is assigned for all the empty spaces.
        This number represents how many neighboring bombs there are.
        """

        # Check every row and column
        for row in range(self.dimension_size):
            for column in range(self.dimension_size):
                # Continue iteration if the space we pass over is already a bomb
                if self.board[row][column] == '*':
                    continue

                self.board[row][column] = self.get_num_neighbor_bombs(row, column)

    def get_num_neighbor_bombs(self, row, column):
        # Recursively iterate through each neighboring position and sum up the number of bombs
        num_neighbor_bombs = 0
        # Max statement ensures the r value never goes below 0, min statement is to ensure that r value never goes 
        # below the dimensions of the game board
        for r in range(max(0, row-1), min(self.dimension_size-1, row+1)+1):
            for c in range(max(0, column-1), min(self.dimension_size-1, column+1)+1):
                if r == row and c == column:
                    # This is an original location, continue iteration
                    continue

                if self.board[r][c] == '*':
                    num_neighbor_bombs += 1

        return num_neighbor_bombs

    def dig(self, row, column):
        # Dig at the defined location

        # If the user hits a bomb, then game over

        # Else recursively dig at a location w/ and w/o neighboring bombs 
        self.dug.add((row, column)) # Keep track of digging locations

        if self.board[row][column] == '*':
            return False
        elif self.board[row][column] > 0:
            return True

        for r in range(max(0, row-1), min(self.dimension_size-1, row+1)+1):
            for c in range(max(0, column-1), min(self.dimension_size-1, column+1)+1):
                # If the spot has already been dug, continue iteration
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        # If print is called on this object,
        # then it'll print out what the function returns

        # Create an array that represents what the user sees
        visible_board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
        for row in range(self.dimension_size):
            for col in range(self.dimension_size):
                if(row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Put this board into a string
        string_representation = ''

        widths = []
        for index in range(self.dimension_size):
            columns = map(lambda x: x[index], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dimension_size)]
        indices_row = '    '
        cells = []
        for index, column in enumerate(indices):
            format = '%-' + str(widths[index]) + "s"
            cells.append(format % (column))

        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_representation += f'{i} |'
            cells = []
            for index, column in enumerate(row):
                format = '%-' + str(widths[index]) + "s"
                cells.append(format % (column))
            string_representation += ' |'.join(cells)
            string_representation += ' |\n'

        str_len = int(len(string_representation) / self.dimension_size)
        string_representation = indices_row + '-'*str_len + '\n' + string_representation + '-'*str_len

        return string_representation

# Play Minesweeper
def play(dimension_size=10, num_bombs=10):
    # Create the game board
    board = Board(dimension_size, num_bombs)
    # Show user the board and ask for user input
    # If the location the user picked is where a bomb is placed, game's over
    # If the location is not where a bomb is, use recursive function to dig in other spots 
    # until each square is next to a bomb
    # Repeat steps 2, 3, and 4 until there are no more bombs
    safe = True
    while len(board.dug) < board.dimension_size**2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Please input as row, column: "))
        row, column = int(user_input[0]), int(user_input[-1])
        # If user input is invalid, prompt for user input again
        if row < 0 or row >= board.dimension_size or column < 0 or column >= dimension_size:
            print("Invalid location. Please enter again")
            continue
        # Else, start digging
        safe = board.dig(row, column)
        if not safe:
            # A bomb as been dug
            break # Game over
    if safe:
        print("You've Won!")
    else:
        print("Game Over :(")
        board.dug = [(r, c) for r in range(board.dimension_size) for c in range(board.dimension_size)]
        print(board)

if __name__ == '__main__':
    play()



