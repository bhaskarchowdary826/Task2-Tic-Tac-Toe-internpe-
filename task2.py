import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                                   command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True

        # Check columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def check_draw(self):
        return all([cell != " " for row in self.board for cell in row])

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
