from experiment import run_experiment, get_optimal_path
from env import CliffWalkingEnv

if __name__ == "__main__":
    print("Testing Q-Learning...")
    q_agent, q_rewards = run_experiment('q_learning', num_episodes=50)
    print(f"Q-Learning Finished. Sample Reward: {q_rewards[-1]}")
    
    print("Testing SARSA...")
    s_agent, s_rewards = run_experiment('sarsa', num_episodes=50)
    print(f"SARSA Finished. Sample Reward: {s_rewards[-1]}")
    
    print("Success!")
