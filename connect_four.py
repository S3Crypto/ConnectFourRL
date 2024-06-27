import numpy as np

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)  # 6 rows, 7 columns board
        self.current_player = 1  # Player 1 starts
        self.score = {1: 0, 2: 0}  # Scoreboard for players

    def display_board(self):
        for row in np.flip(self.board, 0):
            print(' '.join(self.get_colored_disc(disc) for disc in row))
        print("\n")

    def get_colored_disc(self, disc):
        if disc == 1:
            return "\033[93mO\033[0m"  # Yellow disc
        elif disc == 2:
            return "\033[91mO\033[0m"  # Red disc
        else:
            return "."

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

    def display_scoreboard(self):
        print(f"Scoreboard: Player 1 (Yellow) {self.score[1]} - Player 2 (Red) {self.score[2]}")