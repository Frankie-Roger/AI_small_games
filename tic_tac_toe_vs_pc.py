import math
import random
import time


def main():
    g = TicTacToe()
    modes(g)

class TicTacToe():

    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
        self.x_score = 0
        self.o_score = 0
        self.tie_score = 0

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    @staticmethod
    def instructions_board():
        print((' ' * 26) + f'0 | 1 | 2 ')
        print(' ' * 25, end='')
        print(('_' * 3), ('_' * 3), ('_' * 3), sep='|')
        print((' ' * 25) + f' 3 | 4 | 5 ')
        print(' ' * 25, end='')
        print(('_' * 3), ('_' * 3), ('_' * 3), sep='|')
        print((' ' * 25) + f' 6 | 7 | 8 \n')

    def print_board(self):
        one = self.board[0]
        two = self.board[1]
        three = self.board[2]
        four = self.board[3]
        five = self.board[4]
        six = self.board[5]
        seven = self.board[6]
        eight = self.board[7]
        nine = self.board[8]
        print(f' {one} | {two} | {three} ')
        print(('_' * 3), ('_' * 3), ('_' * 3), sep='|')
        print(f' {four} | {five} | {six} ')
        print(('_' * 3), ('_' * 3), ('_' * 3), sep='|')
        print(f' {seven} | {eight} | {nine} ')
        print((' ' * 3), (' ' * 3), (' ' * 3), sep='|', end='\n\n')
        return

    def rules(self):

        self.instructions_board()
        print("""Answer using numbers from 1 to 9,
to indicate the spot that you wanna mark.
Following the logic in the example above.

""")

    def reset(self):
        self.current_winner = None
        self.board = self.make_board()

    def reset_score(self):
        self.x_score = 0
        self.o_score = 0
        self.tie_score = 0

    def print_score(self):
        print(f"\nPlayer 'x' won {self.x_score} times, player 'o' won {self.o_score} times "
              f"and you guys tied {self.tie_score} times.\n\n")

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, letter):
        if self.board[0] == letter and self.board[1] == letter and self.board[2] == letter:
            return True
        if self.board[3] == letter and self.board[4] == letter and self.board[5] == letter:
            return True
        if self.board[6] == letter and self.board[7] == letter and self.board[8] == letter:
            return True
        if self.board[0] == letter and self.board[3] == letter and self.board[6] == letter:
            return True
        if self.board[1] == letter and self.board[4] == letter and self.board[7] == letter:
            return True
        if self.board[2] == letter and self.board[5] == letter and self.board[8] == letter:
            return True
        if self.board[0] == letter and self.board[4] == letter and self.board[8] == letter:
            return True
        if self.board[2] == letter and self.board[4] == letter and self.board[6] == letter:
            return True
        else:
            return False

    def empty_squares(self):
        if self.board.count(' ') == 9:
            return True
        else:
            return False

    def no_empty_squares(self):
        if self.board.count(' ') == 0:
            return True
        else:
            return False

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']


def play(game, player_x, player_o, print_rules=True, inverted=False):
    game.reset()
    if print_rules:
        game.rules()
        game.print_board()

    if inverted:
        letter = 'o'
    else:
        letter = 'x'
    while True:
        print(f'Player "{letter}" turn:')
        if letter == 'o':
            move = player_o.get_move(game)
        else:
            move = player_x.get_move(game)
        game.make_move(move, letter)
        if game.current_winner:
            game.print_board()
            print(f"\n\nPlayer {letter} wins!!!\n\n")
            return letter
        elif game.no_empty_squares():
            if game.tie_score <= 10:
                game.print_board()
                print("\n\nIt's a tie!\nTry again.\n\n")
                time.sleep(.4)
                game.tie_score += 1
                game.reset()
            else:
                print("You guys tied 10 times in a row.I'm afraid there is no use...\nTo next time 👋 ")
                break
        else:
            game.print_board()
        letter = 'o' if letter == 'x' else 'x'
        time.sleep(.7)


def modes(game):
    again = ''
    print("WELCOME TO TIC TAC TOE!\n")
    while again != 'no':
        while True:
            mode = input("""
            Would you like to play alone? (insert: '1p')
            With a friend?  (insert: '2p')
            Or between AI? (insert: 'ai')\n\n--> """).lower().strip()
            if mode == 'alone' or mode == '1p':
                while True:
                    x_or_o = ''
                    x_p = input("Wanna be 'x' or 'o'? \n").lower().strip()
                    if x_p == 'x':
                        x_p = HumanPlayer('x')
                        x_or_o = 'o'
                        break
                    elif x_p == 'o':
                        o_p = HumanPlayer('o')
                        x_or_o = 'x'
                        break
                    else:
                        raise print("Please only insert 'x' or 'o'")
                while True:
                    diff = input("Do you want the computer to be:\neasy,\nmedium,\nhard,\nhardcore.\n").lower().strip()
                    if diff == 'easy':
                        if x_or_o == 'x':
                            x_p = Easy_AI_Player('x')
                            break
                        else:
                            o_p = Easy_AI_Player('o')
                            break
                    elif diff == 'medium':
                        if x_or_o == 'x':
                            x_p = Medium_AI_Player('x')
                            break
                        else:
                            o_p = Medium_AI_Player('o')
                            break
                    elif diff == 'hard':
                        if x_or_o == 'x':
                            x_p = Hard_AI_Player('x')
                            break
                        else:
                            o_p = Hard_AI_Player('o')
                            break
                    elif diff == 'hardcore':
                        if x_or_o == 'x':
                            x_p = Hardcore_AI_Player('x')
                            break
                        else:
                            o_p = Hardcore_AI_Player('o')
                            break
                    else:
                        print('Sorry what? The options are: \neasy,\nmedium,\nhard,\nhardcore')
                break
            elif mode == 'ai':
                while True:
                    diff = input(
                        "Do you want the computer 'x' to be:\neasy,\nmedium,\nhard,\nhardcore.\n\n").lower().strip()
                    if diff == 'easy':
                        x_p = Easy_AI_Player('x')
                        break
                    elif diff == 'medium':
                        x_p = Medium_AI_Player('x')
                        break
                    elif diff == 'hard':
                        x_p = Hard_AI_Player('x')
                        break
                    elif diff == 'hardcore':
                        x_p = Hardcore_AI_Player('x')
                        break
                    else:
                        print('Sorry what? The options are: \neasy,\nmedium,\nhard,\nhardcore')
                while True:
                    diff = input(
                        "Do you want the computer 'o' to be:\neasy,\nmedium,\nhard,\nhardcore.\n\n").lower().strip()
                    if diff == 'easy':
                        o_p = Easy_AI_Player('o')
                        break
                    elif diff == 'medium':
                        o_p = Medium_AI_Player('o')
                        break
                    elif diff == 'hard':
                        o_p = Hard_AI_Player('o')
                        break
                    elif diff == 'hardcore':
                        o_p = Hardcore_AI_Player('o')
                        break
                    else:
                        print('Sorry what? The options are: \neasy,\nmedium,\nhard,\nhardcore')
                break
            elif mode == 'with a friend' or mode == '2p':
                x_p = HumanPlayer('x')
                o_p = HumanPlayer('o')
                break
            else:
                print("I don't understand, please only insert: '1p', '2p' or 'ai'.")
        game.reset()
        p_won = play(game, x_p, o_p)
        if p_won == 'x':
            game.x_score += 1
            game.print_score()
        elif p_won == 'o':
            game.o_score += 1
            game.print_score()
        while True:
            again = input("Wanna go again?\n").lower().strip()
            if again == 'yes':
                chane_mode = input("Do you want do change the game mode?\n").lower().strip()
                if chane_mode == 'yes':
                    game.reset_score()
                    break
                else:
                    game.reset()
                    p_won = play(game, x_p, o_p)
                    if p_won == 'x':
                        game.x_score += 1
                        game.print_score()
                    elif p_won == 'o':
                        game.o_score += 1
                        game.print_score()
            else:
                print("Thanks for playing. See ya 👋")
                break


class Player():

    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        global spot
        valid_square = False
        game.instructions_board()
        while not valid_square:
            try:
                spot = int(input('What spot do you want to mark? ').strip())
                if spot not in game.available_moves():
                    raise ValueError
                else:
                    valid_square = True
            except ValueError:
                print("Square is not valid, try again")
        return spot


class Easy_AI_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        moves = []
        for _ in range(10):
            m = random.choice(game.available_moves())
            moves.append(m)
        square = random.choice(moves)
        print(f"{self.letter} moves to spot {square}")
        return square


class Hardcore_AI_Player(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        print(f"{self.letter} moves to spot {square}")
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'o' if player == 'x' else 'x'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            n_other = -1 * (state.num_empty_squares() + 1)
            return {'position': None, 'score': n_other}
        elif state.current_winner == max_player:
            n_max = +1 * (state.num_empty_squares() + 1)
            return {'position': None, 'score': n_max}
        elif state.no_empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


class Hard_AI_Player(Hardcore_AI_Player):

    def __init__(self, letter):
        super().__init__(letter)
        self.count = 0

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            self.count = 0
        if self.count % 2 == 0:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        self.count += 1
        print(f"{self.letter} moves to spot {square}")
        return square


class Medium_AI_Player(Hardcore_AI_Player):

    def __init__(self, letter):
        super().__init__(letter)
        self.count = 0

    @staticmethod
    def multiples(value, length):
        return [value * i for i in range(1, length + 1)]

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            self.count = 0
        if self.count % 2 == 0 or self.count in self.multiples(3, 50):
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        self.count += 1
        print(f"{self.letter} moves to spot {square}")
        self.count += 1
        print(f"{self.letter} moves to spot {square}")
        return square


if __name__ == '__main__':
    main()
