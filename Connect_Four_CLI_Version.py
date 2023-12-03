import numpy as np
import os

class ConnectFourBoard:
    # The 'char' list represents the characters used to display the game board.
    char = [" ", "X", "O"]
    # The 'grid' attribute is a 6x7 numpy array that represents the game board. It is initialized with zeros.
    def __init__(self):
        self.grid = np.zeros((6, 7), dtype=int)
    # This method prints the current state of the game board. It iterates over each row and column of the 'grid' attribute and prints the corresponding character from the 'char' list.  
    def print(self):
        for row in range(5, -1, -1):
            print("|", end=" ")
            for col in range(7):
                print(self.char[self.grid[row][col]], end=" | ")
            print("\n+" + 29 * "-" + "+")
        
    # Prints the column numbers for reference.
        print("  1   2   3   4   5   6   7")
        
    # This method returns the values in the specified column of the game board.
    def get_value(self, col):
        return self.grid[:, col]
        
    # This method sets the value in the specified column and the first available row in the game board.
    def set_value(self, col, value):
        for row in range(6):
            if self.grid[row][col] == 0:
                self.grid[row][col] = value
                break
        
    # This method checks if there is a horizontal victory condition on the game board.
    def check_victory(self):
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if (self.grid[row][col] == self.grid[row][col + 1] == self.grid[row][col + 2] == self.grid[row][col + 3] != 0):
                    return True
        

        # This method checks if there is a vertical victory condition on the game board.
        for row in range(3):
            for col in range(7):
                if (self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] != 0):
                    return True
        

       # This method checks if there is a positive diagonal victory condition on the game board.
        for row in range(3):
            for col in range(4):
                if (self.grid[row][col] == self.grid[row + 1][col + 1] == self.grid[row + 2][col + 2] == self.grid[row + 3][col + 3] != 0):
                    return True
        

        # This method checks if there is a negative diagonal victory condition on the game board.
        for row in range(3, 6):
            for col in range(4):
                if (self.grid[row][col] == self.grid[row - 1][col + 1] == self.grid[row - 2][col + 2] == self.grid[row - 3][col + 3] != 0):
                    return True
        

        return False
        
        # This method checks if the game board is full.
    def is_full(self):
        return not any(0 in row for row in self.grid)
        
        # This method resets the game board by filling it with zeros.
    def reinit(self):
        self.grid.fill(0)
       
        # The 'players' list represents the players in the game.
class ConnectFour:
    players = ["O", "X"]
    
        # The 'turn' attribute represents the current turn number.
    def __init__(self):
        self.turn = 1
        # The 'board' attribute is an instance of the 'ConnectFourBoard' class.
        self.board = ConnectFourBoard()
      
        # Prints the current turn number and the player whose turn it is, then prints the game board.
    def launch_game(self):
        while True:
            print(20 * "*")
            print("Turn", self.turn, ": Player", self.players[self.turn % 2])
            print(20 * "*")
            self.board.print()
           
        # Prompts the current player to enter their move (column number). If the move is valid (within the range of 0 to 6) and the selected column is not full, the move is set on the game board. Otherwise, an error message is printed.

            col = int(input("Enter your move: ")) - 1
            if 0 <= col <= 6:
                if self.board.get_value(col)[5] == 0:
                    self.board.set_value(col, 2 - (self.turn % 2))
                else:
                    print("Column", col + 1, "is full, please, choose another column.")
                    continue
            else:
                print("Invalid column number, please choose a column between 1 and 7.")
                continue
            # Checks if there is a victory condition or if the game is a draw. If either condition is met, the game ends and the corresponding message is printed.
            if self.turn >= 7 and self.board.check_victory():
                os.system('cls')
                print("Player", self.players[self.turn % 2], "won!")
                self.board.print()
                break
            elif self.turn >= 42:
                os.system('cls')
                print("The game is a draw!")
                self.board.print()
                break
            
            
            
            # Increments the turn number and clears the console screen.
            self.turn += 1
            os.system('cls')
            # Asks the user if they want to play another game. If yes, the game board is reset and a new game is launched.
        answer = input("Do you want to play another game? (Y/N)").upper()
        if answer == "Y":
            os.system('cls')
            self.board.reinit()
            self.turn = 1
            self.launch_game()
        
        
game = ConnectFour()
game.launch_game()

