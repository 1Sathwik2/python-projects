import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.window = tk.Tk()
        self.window.title("TicTacToe")

        self.buttonsGrid = []
        for i in range(3):
            row = []
            for j in range(3):
                # where to insert this button , text on button
                #i, j var are created and given values acc to loop and are passed to func/behaviour when we click the button
                button = tk.Button(self.window, text="", width = 20, height = 10, command = lambda i=i, j=j : self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttonsGrid.append(row)
    
   

    def check_winner(self, player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:# checking rows are same
                return True
            elif player == self.board[0][i] == self.board[1][i] == self.board[2][i]:# checking cols are same
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
        elif player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
        else:
             return False
        
    def is_draw(self):
         for row in self.board:
              if "" in row:
                   return False
         return True
            

    def make_move(self, row, column):
        if self.board[row][column] == "":
            self.board[row][column] = self.current_player
            self.buttonsGrid[row][column].config(text = self.current_player) 

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game over", "the winner is " + self.current_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("Game over", "the match is draw")
                self.window.quit()


            self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        self.window.mainloop()



game = TicTacToe()
game.run()
othergame = TicTacToe()
othergame.run()