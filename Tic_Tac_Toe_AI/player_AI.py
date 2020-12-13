import math
import random

class Player:
    def __init__(self, letter):
        # Letter is either X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn to make a move from (0-8): ')
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("You have entered an incorrect input, please try again")
        
        return value

# Write a function for the AI
class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # This function is where the magic happens
    def get_move(self, game):
        # If all spaces are available on the board, find a random spot
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # 
        else:
            # Get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']

        return square
    
    def minimax(self, state, player):
        """ 
        The minimax function will attempt to find the best possible scenario for the human player to move
        and simulate how each of the player's next moves will determine if they win or not
        """
        max_player = self.letter # The human player
        other_player = 'O' if player == 'X' else 'X'

        # First check if a player has already won
        # These are base cases
        if state.current_winner == other_player:
            # Return the position, score to keep track of the current score
            return {
                    'position': None,
                    'score': 1 * (state.number_empty_squares() + 1) if other_player == max_player else -1 *(
                        state.number_empty_squares() + 1)
                }
        # If there are no empty squares left
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # These are special cases for minimax implementation
        if player == max_player:
            # The following variable will keep track of the best position and the best score to help the player win
            best = {'position': None, 'score': -math.inf} # Each score should be greater than -infinity
        else:
            best = {'position': None, 'score': math.inf} # Each score should minimize and be less than infinity

        for move in state.available_moves():
            # Make a move and attempt to take that spot
            state.make_move(move, player)
            # Find a simulated score to see how will the move determine the player's score
            simulated_score = self.minimax(state, other_player)
            # Undo that simulated move
            state.board[move] = ' '
            state.current_winner = None
            simulated_score['position'] = move

            # Update dictionaries
            if player == max_player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score # Replace the best score for the human player
                else:
                    if simulated_score['score'] < best['score']:
                        best = simulated_score # Replace the best score for the AI

        return best
