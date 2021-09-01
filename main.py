from game_logic import Game


def print_help():
    print("""
___HELP:___
Start   --> starts the game.
Restart --> restarts the game.
End     --> stops the game.

    """)


if __name__ == '__main__':
    print("""
Tic Tac Toe
(c) Paschalis Ilias
emain: ilias2002vip.gr@gmail.com

Type 'start' to begin.
Type 'help' for help.
    """)

    while True:
        cmd = input(">").lower()
        if cmd == "start":
            game = Game()
            game.play_game()
        elif cmd == "end":
            break
        else:
            print_help()
