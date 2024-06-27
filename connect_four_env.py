import gymnasium as gym
from gymnasium import spaces
import numpy as np

class ConnectFourEnv(gym.Env):
    def __init__(self):
        super(ConnectFourEnv, self).__init__()
        
        # Define action and observation space
        self.action_space = spaces.Discrete(7)
        
        # Flatten the observation space to a 1D vector
        self.observation_space = spaces.Box(low=0, high=2, shape=(6 * 7,), dtype=int)
        
        self.board = np.zeros((6, 7), dtype=int)
        self.current_player = 1
        self.done = False
        self.winner = None

    def reset(self, seed=None, options=None):
        # Set the seed for reproducibility
        if seed is not None:
            self.np_random, seed = gym.utils.seeding.np_random(seed)

        self.board = np.zeros((6, 7), dtype=int)
        self.current_player = 1
        self.done = False
        self.winner = None
        return self.board.flatten(), {}

    def step(self, action):
        if self.done:
            raise ValueError("Cannot step in a finished environment")
        
        if self.board[5, action] != 0:
            # Invalid move (column is full), return current state and a high negative reward
            return self.board.flatten(), -10, True, False, {}
        
        # Drop the disc in the selected column
        for row in range(6):
            if self.board[row, action] == 0:
                self.board[row, action] = self.current_player
                break
        
        # Check for a win or tie
        if self._check_winner(self.current_player):
            self.done = True
            self.winner = self.current_player
            return self.board.flatten(), 10, True, False, {}
        
        if self._is_board_full():
            self.done = True
            return self.board.flatten(), 0, True, False, {}  # Tie

        # Switch players
        self.current_player = 3 - self.current_player
        
        return self.board.flatten(), 0, False, False, {}

    def _check_winner(self, player):
        # Check horizontal, vertical, and diagonal (both directions) for a win
        for c in range(7 - 3):
            for r in range(6):
                if self.board[r, c] == player and self.board[r, c+1] == player and self.board[r, c+2] == player and self.board[r, c+3] == player:
                    return True
        
        for c in range(7):
            for r in range(6 - 3):
                if self.board[r, c] == player and self.board[r+1, c] == player and self.board[r+2, c] == player and self.board[r+3, c] == player:
                    return True

        for c in range(7 - 3):
            for r in range(6 - 3):
                if self.board[r, c] == player and self.board[r+1, c+1] == player and self.board[r+2, c+2] == player and self.board[r+3, c+3] == player:
                    return True

        for c in range(7 - 3):
            for r in range(3, 6):
                if self.board[r, c] == player and self.board[r-1, c+1] == player and self.board[r-2, c+2] == player and self.board[r-3, c+3] == player:
                    return True

        return False

    def _is_board_full(self):
        return all(self.board[5, col] != 0 for col in range(7))

    def render(self, mode='human'):
        # Print the board to the console
        print(np.flip(self.board, 0))

    def close(self):
        pass
