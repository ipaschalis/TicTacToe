# TicTacToe
A small game for me to practice programing.

## How to play:
___

* First run the main.py. Then type start to start a new game.
* Once the game has started, the player is asked to give the X and Y coordinences to place their mark on the board.

## To be added:
___
* Score counter.
* Ability for zeroing of the score counter.

## About the source code:
___

Feel free to use parts of my code to make your own game, but if you do so I want you to credit me.

The game logic is broken down to simple function, so that someone could call them in their own program or easily modify the way the game is played. Theoretically, someone could write a program that has many instances of the Game running simultaneously, maybe in a discord bot.

## How to interact with the class Game():
___
### __ init__()
___
This function is called when you create a new object of the class Game().

**What it does is:**
1. Creates an empty list named ***board***, in which the game will be played.
2. Creates an empty string named ***player_playing***, which points who is currently playing (x/o).
3. Creates a string named ***winner***, this string shows if there is a winner or not and who it is. - means no winner, x means that player x has won and o means that player o has won.
4. Creates a 2D list named ***coordinates***, which is later printed to help the player know what are the coordinates they need to type in order to put their mark on the board.
5. Creates a 2D list named ***new_board***, this list is later copied each time you want to start a new game.
6. Creates two strings named ***player_one*** and ***player_two*** where the marks **x** and **o** are stored. In the feature there will be the ability to set you own marks.
7. Creates a int named ***moves_made***, which works as a counter for how many valid moves have being made.

### Getters:
___
Those functions return the values of the variables of the class that were created in the __ init__() function:
* **get_board()**
* **get_player_playing()**
* **get_winner()**
* **get_coordinates()**
* **get_new_board()**
* **get_player_one()**
* **get_player_two()**
* **get_moves_made()**

### Setters:
___
Those functions return the values of the variables of the class that were created in the __ init__() function:
* **set_board()**
* **set_player_playing()**
* **set_winner()**
* **set_player_one()**
* **set_player_two()**
* **set_moves_made()**

### next_player()
___
This function changes the ***player_playing*** between ***player_one*** and ***player_two***.

### display_board()
___
This function displays the ***board*** in a way that the players can easily visualise.

**For example:**
````
['x', '-', '-']

['o', 'x', '-']

['-', '-', 'o']
````

### do_move(x, y)
___
This function gets the X and Y coordinates and firstly checks if that place on the ***board*** is empty; if yes it places there the mark of the ***player_playing*** and *returns* **True** (aka that the move happened); if that place on the board contains a mark of any of the players, then it simply *returns* **False** (aka the move didn't happen).

### check_for_win()
___
This function checks if one of the players has won. If yes it puts the mark of the ***player_playing*** into ***winner***.

### new_game()
___

This function creates a new game by:
1. Copies ***new_board*** into ***board***, aka clears the board for a new game.
2. Sets ***player_one*** as the ***player_playing***.
3. Sets the ***winner*** to "-", aka there is no winner.
4. Sets ***moves_made*** to 0.

### play_game()
___
This function creates a new game session. It handles the user interface and calls other functions to control the game logic and the flow of the game.

**How it works:**
1. Sets up a new game.
2. Displays to the payers the ***coordinates*** so that they know what to type later.
3. Displays whose turn is to play.
4. Displays the ***board***
5. Asks the player to say were they want to put their mark (X, Y).
6. Checks if X and Y are valid coordinates.
7. If yes it checks if the move is a valid move and if it is it does it and changes to the next player.
8. If it is not a valid move, it asks the player to give again the coordinates and repeats 5 to 8 until a valid move is made.
9. Checks that the game hasn't come to a draw.
10. Repeats 3 to 9 until one of the players wins. Then it displays the winner or says that there is a draw.

*Currently, the game doesn't keep a scour. 

**Example of how to call it:**
````
from game_logic import Game 

game = Game()
game.play_game()
````
___