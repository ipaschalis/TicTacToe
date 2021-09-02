"""
Tic Tac Toe
(c) Paschalis Ilias
email: ilias2002vip.gr@gmail.com"""


class Game:

    def __init__(self):
        self.board = []
        self.player_playing = ""
        self.winner = "-"
        self.coordinates = [["(0, 0)", "(0, 1)", "(0, 2)"], ["(1, 0)", "(1, 1)", "(1, 2)"], ["(2, 0)", "(2, 1)", "(2, 2)"]]
        self.new_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.player_one = "x"
        self.player_two = "o"
        self.moves_made = 0

    # Getters:

    def get_board(self):
        return self.board

    def get_player_playing(self):
        return self.player_playing

    def get_winner(self):
        return self.winner

    def get_coordinates(self):
        return self.coordinates[:]

    def get_new_board(self):
        return self.new_board[:]

    def get_player_one(self):
        return self.player_one

    def get_player_two(self):
        return self.player_two

    def get_moves_made(self):
        return self.moves_made

    # Setters:

    def set_board(self, board):
        self.board = board

    def set_player_playing(self, player_playing):
        self.player_playing = player_playing

    def set_winner(self, winner):
        self.winner = winner

    def set_player_one(self, player_one):
        self.player_one = self.player_one

    def set_player_two(self, player_two):
        self.player_two = player_two

    def set_moves_made(self, moves_made):
        self.moves_made =moves_made

    # Game logic:

    def next_player(self):
        if self.player_playing == self.player_one:
            self.player_playing = self.player_two
        else:
            self.player_playing = self.player_one

    def display_board(self):
        for i in range(3):
            print(self.board[i])

    def do_move(self, x, y):
        if self.board[x][y] == "-":
            self.board[x][y] = self.player_playing
            return True
        else:
            return False

    def check_for_win(self):
        if self.board[0] == ["x", "x", "x"] or self.board[1] == ["x", "x", "x"] or self.board[2] == ["x", "x", "x"]:
            self.winner = "x"
        elif self.board[0] == ["o", "o", "o"] or self.board[1] == ["o", "o", "o"] or self.board[2] == ["o", "o", "o"]:
            self.winner = "o"

        elif self.board[0][0] == "x" and self.board[1][0] == "x" and self.board[2][0] == "x":
            self.winner = "x"
        elif self.board[0][1] == "x" and self.board[1][1] == "x" and self.board[2][1] == "x":
            self.winner = "x"
        elif self.board[0][2] == "x" and self.board[1][2] == "x" and self.board[2][2] == "x":
            self.winner = "x"
        elif self.board[0][0] == "o" and self.board[1][0] == "o" and self.board[2][0] == "o":
            self.winner = "o"
        elif self.board[0][1] == "o" and self.board[1][1] == "o" and self.board[2][1] == "o":
            self.winner = "o"
        elif self.board[0][2] == "o" and self.board[1][2] == "o" and self.board[2][2] == "o":
            self.winner = "o"

        elif self.board[0][0] == "x" and self.board[1][1] == "x" and self.board[2][2] == "x":
            self.winner = "x"
        elif self.board[2][0] == "x" and self.board[1][1] == "x" and self.board[0][2] == "x":
            self.winner = "x"
        elif self.board[0][0] == "o" and self.board[1][1] == "o" and self.board[2][2] == "o":
            self.winner = "o"
        elif self.board[2][0] == "o" and self.board[1][1] == "o" and self.board[0][2] == "o":
            self.winner = "o"

        else:
            self.winner = "-"

    def new_game(self):
        self.board = self.new_board[:]
        self.player_playing = self.player_one
        self.winner = "-"
        self.moves_made = 0

    def play_game(self):
        self.new_game()
        print("""X and Y values:
        """)
        for i in range(3):
            print(self.coordinates[i])
            print("")

        while self.winner == "-":
            print("")
            print("_________________________________")
            print(f"Player playing: {self.player_playing.upper()}")

            print("")
            self.display_board()

            print("")
            x = int(input(f"Give X coordinate for player {self.player_playing}: "))
            y = int(input(f"Give Y coordinate for player {self.player_playing}: "))
            if 0 <= x < 3 and 0 <= y < 3 and self.do_move(x, y):
                self.check_for_win()
                if self.moves_made < 9:
                    self.moves_made += 1
                    self.next_player()
                else:
                    self.winner = "DRAW"
                # print(f"the current winner is {self.winner}")
            else:
                print("""
INVALID MOVE!!!
Try again!""")
        if self.winner != "DRAW":
            print(f"The winner is: {self.winner.upper()}")
        else:
            print("Its a draw, better luck the next time!")


if __name__ == '__main__':
    game = Game()
    game.play_game()
    """game.do_move(0, 0, "x")
    game.do_move(0, 1, "x")
    game.do_move(1, 2, "x")
    print(game.check_for_win())
    print(game.get_board())"""
