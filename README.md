# ConnectFour_Game_Class_Based_CLI_Version
The provided code is an implementation of the Connect Four game using Python and the numpy library. It consists of two classes: `ConnectFourBoard` and `ConnectFour`.

The `ConnectFourBoard` class represents the game board. It has the following attributes and methods:

- `char`: A list that represents the characters used to display the game board.
- `grid`: A 6x7 numpy array that represents the game board. It is initialized with zeros.
- `print()`: A method that prints the current state of the game board.
- `get_value(col)`: A method that returns the values in the specified column of the game board.
- `set_value(col, value)`: A method that sets the value in the specified column and the first available row in the game board.
- `check_victory()`: A method that checks if there is a victory condition on the game board.
- `is_full()`: A method that checks if the game board is full.
- `reinit()`: A method that resets the game board by filling it with zeros.

The `ConnectFour` class represents the Connect Four game. It has the following attributes and methods:

- `players`: A list that represents the players in the game.
- `turn`: An attribute that represents the current turn number.
- `board`: An instance of the `ConnectFourBoard` class.
- `launch_game()`: A method that starts the game and handles the game logic.

The `launch_game()` method runs an infinite loop that prompts the current player to enter their move (column number). It checks if the move is valid and sets it on the game board. It then checks if there is a victory condition or if the game is a draw. If either condition is met, the game ends and the corresponding message is printed. The turn number is incremented, and the console screen is cleared. The user is then asked if they want to play another game.
