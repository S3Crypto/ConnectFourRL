import matplotlib.pyplot as plt
import numpy as np
from stable_baselines3 import PPO
from connect_four_env import ConnectFourEnv  # Adjust import as per your file structure

# Initialize environment and model
env = ConnectFourEnv()
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)

# Evaluate model and collect episode information
num_episodes = 100
ep_rewards = []
for _ in range(num_episodes):
    obs = env.reset()
    ep_reward = 0
    done = False
    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        ep_reward += reward
    ep_rewards.append(ep_reward)

# Plot episode rewards
plt.plot(np.arange(1, num_episodes + 1), ep_rewards)
plt.xlabel('Episode')
plt.ylabel('Episode Reward')
plt.title('Episode Rewards over Evaluation')
plt.grid(True)
plt.show()
