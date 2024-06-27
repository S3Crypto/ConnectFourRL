import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from connect_four_env import ConnectFourEnv

# Function to evaluate model performance
def evaluate_model(model, env, num_episodes=100):
    win_count = 0
    episode_lengths = []
    for _ in range(num_episodes):
        obs = env.reset()
        done = False
        episode_length = 0
        while not done:
            action, _ = model.predict(obs)
            obs, _, done, info = env.step(action)  # Capture `info` returned by step
            episode_length += 1
        episode_lengths.append(episode_length)
        # Access 'winner' from info dictionary
        if info[0]['winner'] == 1:  # Assuming player 1 is the model being evaluated
            win_count += 1
    win_rate = win_count / num_episodes
    avg_game_length = np.mean(episode_lengths)
    return win_rate, avg_game_length

# Create Connect Four environment
env = ConnectFourEnv()
env = DummyVecEnv([lambda: env])

# Initialize PPO model
model = PPO('MlpPolicy', env, verbose=1)

# Train the model
num_timesteps = int(1e5)
model.learn(total_timesteps=num_timesteps)

# Evaluate the trained model
win_rate, avg_game_length = evaluate_model(model, env, num_episodes=100)

print(f"Win rate: {win_rate:.2f}")
print(f"Average game length: {avg_game_length:.2f} moves")

# Plot learning curve
plt.plot(np.arange(1, num_timesteps+1), model.ep_info_buffer)
plt.xlabel('Timesteps')
plt.ylabel('Episode Reward')
plt.title('PPO Learning Curve')
plt.show()

# Save the trained model
model.save("connect_four_ppo")

# Close the environment
env.close()
