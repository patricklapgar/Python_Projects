from player_AI import HumanPlayer, AIComputerPlayer, RandomComputerPlayer

class Tic_Tac_Toe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Create the game board
        self.current_winner = None # Keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        # Tells which number corresponds to a spot on the game board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def number_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if there are 3 spots filled with the same letter anywhere on the board
        
        # Check rows first
        row_index = square // 3
        row = self.board[row_index*3: (row_index + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # If there's no win in rows, then check columns
        column_index = square % 3
        column = [self.board[column_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # If that doesn't work, then check diagonals
        if square % 2 == 0:
            diagonal_left_right = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_left_right]):
                return True
            diagonal_right_left = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_right_left]):
                return True

        return False
def play(game, x_player, o_player, print_game=True):
    # Returns the winner of the game or None for a tie game
    if print_game:
        game.print_board_numbers()

    # Starting letter
    starting_letter = 'X'
    
    # While the game has not been finished, iterate until there's a winner
    while game.empty_squares():
        if starting_letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, starting_letter):
            if print_game:
                print(starting_letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(starting_letter + ' wins')
                return starting_letter

            starting_letter = 'O' if starting_letter == 'X' else 'X'
        else:
            print('It\'s a tie!')

if __name__ == '__main__':
    print("Game Started")
    x_player = RandomComputerPlayer('X')
    o_player = AIComputerPlayer('O')
    tic_tac_toe = Tic_Tac_Toe()
    play(tic_tac_toe, x_player, o_player, print_game=True)