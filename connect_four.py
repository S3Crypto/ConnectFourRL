import tkinter as tk
from tkinter import messagebox
import numpy as np

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)  # 6 rows, 7 columns board
        self.current_player = 1  # Player 1 starts
        self.score = {1: 0, 2: 0}  # Scoreboard for players

    def drop_disc(self, column):
        for row in range(6):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                return True
        return False  # Column is full

    def switch_player(self):
        self.current_player = 3 - self.current_player  # Switch between 1 and 2

    def is_winning_move(self, player):
        for c in range(4):
            for r in range(6):
                if self.board[r][c] == player and self.board[r][c+1] == player and self.board[r][c+2] == player and self.board[r][c+3] == player:
                    return True

        for c in range(7):
            for r in range(3):
                if self.board[r][c] == player and self.board[r+1][c] == player and self.board[r+2][c] == player and self.board[r+3][c] == player:
                    return True

        for c in range(4):
            for r in range(3):
                if self.board[r][c] == player and self.board[r+1][c+1] == player and self.board[r+2][c+2] == player and self.board[r+3][c+3] == player:
                    return True

        for c in range(4):
            for r in range(3, 6):
                if self.board[r][c] == player and self.board[r-1][c+1] == player and self.board[r-2][c+2] == player and self.board[r-3][c+3] == player:
                    return True

        return False

    def is_full(self):
        return all(self.board[5][col] != 0 for col in range(7))  # Top row is full

    def reset_board(self):
        self.board = np.zeros((6, 7), dtype=int)

    def update_score(self, winner):
        if winner in self.score:
            self.score[winner] += 1

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.game = ConnectFour()
        self.buttons = []
        self.create_board()
        self.update_display()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()
        
        # Create column buttons for dropping discs
        for col in range(7):
            button = tk.Button(frame, text=f"Col {col+1}", command=lambda c=col: self.handle_move(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)
        
        # Create the game board grid
        self.board_labels = [[tk.Label(frame, text='.', font=('Arial', 24), width=4, height=2, relief="solid", borderwidth=1)
                              for _ in range(7)] for _ in range(6)]
        
        for r in range(6):
            for c in range(7):
                self.board_labels[r][c].grid(row=r+1, column=c)

        # Create reset and quit buttons
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        quit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def handle_move(self, column):
        if self.game.drop_disc(column):
            self.update_display()
            if self.game.is_winning_move(self.game.current_player):
                messagebox.showinfo("Connect Four", f"Player {self.game.current_player} wins!")
                self.game.update_score(self.game.current_player)
                self.update_scoreboard()
                self.reset_board()
            elif self.game.is_full():
                messagebox.showinfo("Connect Four", "It's a tie!")
                self.reset_board()
            else:
                self.game.switch_player()
        else:
            messagebox.showwarning("Connect Four", "Column is full. Try another column.")

    def update_display(self):
        for r in range(6):
            for c in range(7):
                disc = self.game.board[r][c]
                if disc == 1:
                    self.board_labels[r][c].config(bg='yellow')
                elif disc == 2:
                    self.board_labels[r][c].config(bg='red')
                else:
                    self.board_labels[r][c].config(bg='white')
        
        self.root.update()

    def reset_board(self):
        self.game.reset_board()
        self.update_display()

    def reset_game(self):
        self.reset_board()
        self.game.score = {1: 0, 2: 0}
        self.update_scoreboard()

    def update_scoreboard(self):
        score_text = f"Player 1 (Yellow): {self.game.score[1]} | Player 2 (Red): {self.game.score[2]}"
        self.root.title(f"Connect Four - {score_text}")

def main():
    root = tk.Tk()
    app = ConnectFourGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
