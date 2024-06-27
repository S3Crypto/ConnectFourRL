import gymnasium as gym
import numpy as np
import logging
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv
from connect_four_env import ConnectFourEnv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the Connect Four environment
env = ConnectFourEnv()

# Check if the environment follows the gymnasium interface
try:
    check_env(env)
    logger.info("Environment passed the check!")
except Exception as e:
    logger.error(f"Environment check failed: {e}")

# Wrap the environment in a DummyVecEnv
env = DummyVecEnv([lambda: env])

# Create the PPO model
logger.info("Creating PPO model...")
model = PPO('MlpPolicy', env, verbose=1)

# Train the model
logger.info("Starting training...")
model.learn(total_timesteps=100000)

# Save the trained model
model.save("connect_four_ppo")
logger.info("Model trained and saved as connect_four_ppo.zip")
