player_one = "x"
player_two = "o"


def new_board():
    return [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


class TTTGame:

    def __init__(self):
        self.board = []

    def get_board(self):
        return self.board

    def new_game(self):
        self.board = new_board()

    def do_move(self, x, y, player):
        if self.board[x][y] == "-":
            self.board[x][y] = player
            return 0
        else:
            return -1

    def check_for_win(self):
        if self.board[0] == ["x", "x", "x"] or self.board[1] == ["x", "x", "x"] or self.board[2] == ["x", "x", "x"]:
            return player_one
        elif self.board[0] == ["o", "o", "o"] or self.board[1] == ["o", "o", "o"] or self.board[2] == ["o", "o", "o"]:
            return player_two
        elif self.board[0][0] == "x" and self.board[0][1] == "x" and self.board[0][2] == "x":
            return player_one
        else:
            return "-"


if __name__ == '__main__':
    game = TTTGame()
    game.new_game()
    game.do_move(0, 0, "x")
    game.do_move(0, 1, "x")
    game.do_move(1, 2, "x")
    print(game.check_for_win())
    print(game.get_board())
