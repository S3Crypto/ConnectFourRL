import gym
import numpy as np

class ConnectFourEnv(gym.Env):
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)  # 6 rows, 7 columns
        self.current_player = 1  # Player 1 starts
        self.winner = None  # Winner status
        self.done = False  # Game completion status

        self.action_space = gym.spaces.Discrete(7)  # 7 possible columns to drop a piece into
        self.observation_space = gym.spaces.Box(low=0, high=2, shape=(6, 7), dtype=int)  # Board state

    def step(self, action):
        # Check if the column is full
        if self.board[0, action] != 0:
            return self.board.copy(), -10, self.done, {'winner': self.winner}  # Invalid move penalty

        # Drop the piece in the column
        for row in range(5, -1, -1):
            if self.board[row, action] == 0:
                self.board[row, action] = self.current_player
                break

        # Check for a winner
        self.done, self.winner = self.check_winner()

        # Reward and observation
        reward = 1 if self.winner == 1 else 0  # Reward 1 if player 1 wins, else 0
        return self.board.copy(), reward, self.done, {'winner': self.winner}

    def reset(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.current_player = 1
        self.winner = None
        self.done = False
        return self.board.copy()

    def check_winner(self):
        # Check rows
        for row in range(6):
            for col in range(4):
                if self.board[row, col] == self.board[row, col + 1] == self.board[row, col + 2] == self.board[row, col + 3] != 0:
                    return True, self.board[row, col]

        # Check columns
        for col in range(7):
            for row in range(3):
                if self.board[row, col] == self.board[row + 1, col] == self.board[row + 2, col] == self.board[row + 3, col] != 0:
                    return True, self.board[row, col]

        # Check diagonals
        for row in range(3):
            for col in range(4):
                if self.board[row, col] == self.board[row + 1, col + 1] == self.board[row + 2, col + 2] == self.board[row + 3, col + 3] != 0:
                    return True, self.board[row, col]
            for col in range(3, 7):
                if self.board[row, col] == self.board[row + 1, col - 1] == self.board[row + 2, col - 2] == self.board[row + 3, col - 3] != 0:
                    return True, self.board[row, col]

        # Check if board is full (draw)
        if np.all(self.board != 0):
            return True, 0

        return False, None

    def render(self, mode='human'):
        for row in range(6):
            print(' | '.join(['X' if cell == 1 else 'O' if cell == 2 else ' ' for cell in self.board[row]]))
            if row < 5:
                print('-' * 29)
        print()
