# ConnectFourRL
Connect Four reinforcement learning game

Files Description
connect_four_env.py
This file defines a custom OpenAI Gym environment for Connect Four. The environment is configured to:

Define action and observation spaces suitable for Connect Four.
Manage game state, including current player, board state, and win conditions.
Handle the reset and step functions for game progression.
train_model.py
This script handles the training of the PPO agent. It:

Initializes the Connect Four environment.
Wraps the environment with DummyVecEnv for vectorized training.
Trains the PPO agent for a specified number of timesteps.
Saves the trained model to ppo_connect_four.zip.
evaluate_model.py
This script evaluates the performance of the trained PPO agent. It:

Loads the trained model from ppo_connect_four.zip.
Evaluates the model over a specified number of episodes to compute the win rate and average game length.
Plots the episode lengths over time using Matplotlib.