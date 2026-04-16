import matplotlib.pyplot as plt
import numpy as np

def plot_rewards(q_rewards, sarsa_rewards, window=10):
    def smooth(data, window):
        return np.convolve(data, np.ones(window)/window, mode='valid')

    plt.figure(figsize=(10, 6))
    plt.plot(smooth(q_rewards, window), label='Q-Learning (Off-policy)', color='red')
    plt.plot(smooth(sarsa_rewards, window), label='SARSA (On-policy)', color='blue')
    plt.title('Cliff Walking: Q-Learning vs SARSA')
    plt.xlabel('Episodes (Smoothed)')
    plt.ylabel('Total Reward')
    plt.ylim(-100, 0)
    plt.legend()
    plt.grid(True)
    return plt

def visualize_grid_path(path, height=4, width=12):
    grid = np.zeros((height, width))
    # 1 for path, 2 for cliff, 3 for start, 4 for goal
    for r, c in path:
        grid[r, c] = 1
    
    # Add cliff
    for col in range(1, width - 1):
        grid[height-1, col] = 2
        
    grid[height-1, 0] = 3
    grid[height-1, width-1] = 4
    
    return grid
