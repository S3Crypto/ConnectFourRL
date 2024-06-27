import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv
from connect_four_env import ConnectFourEnv

# Create the Connect Four environment
env = ConnectFourEnv()

# Check if the environment follows the gym interface
check_env(env)

# Wrap the environment in a DummyVecEnv
env = DummyVecEnv([lambda: env])

# Create the PPO model
model = PPO('MlpPolicy', env, verbose=1)

# Train the model
model.learn(total_timesteps=100000)

# Save the trained model
model.save("connect_four_ppo")

print("Model trained and saved as connect_four_ppo.zip")
