from env import CliffWalkingEnv
from agents import QLearningAgent, SarsaAgent
import numpy as np

def run_experiment(agent_type='q_learning', num_episodes=500, alpha=0.1, gamma=0.9, epsilon=0.1):
    env = CliffWalkingEnv()
    num_states = env.get_num_states()
    num_actions = 4
    
    if agent_type == 'q_learning':
        agent = QLearningAgent(num_states, num_actions, alpha, gamma, epsilon)
    else:
        agent = SarsaAgent(num_states, num_actions, alpha, gamma, epsilon)
        
    rewards_per_episode = []
    
    for episode in range(num_episodes):
        state = env.reset()
        state_idx = env.state_to_idx(state)
        total_reward = 0
        done = False
        
        if agent_type == 'sarsa':
            action = agent.choose_action(state_idx)
            
        while not done:
            if agent_type == 'q_learning':
                action = agent.choose_action(state_idx)
                next_state, reward, done = env.step(action)
                next_state_idx = env.state_to_idx(next_state)
                agent.update(state_idx, action, reward, next_state_idx, done)
            else:
                next_state, reward, done = env.step(action)
                next_state_idx = env.state_to_idx(next_state)
                next_action = agent.choose_action(next_state_idx)
                agent.update(state_idx, action, reward, next_state_idx, next_action, done)
                action = next_action
                
            state_idx = next_state_idx
            total_reward += reward
            
        rewards_per_episode.append(total_reward)
        
    return agent, rewards_per_episode

def get_optimal_path(agent, env):
    state = env.reset()
    path = [state]
    done = False
    max_steps = 100 # Prevent infinite loops
    steps = 0
    
    while not done and steps < max_steps:
        state_idx = env.state_to_idx(state)
        action = np.argmax(agent.q_table[state_idx])
        state, _, done = env.step(action)
        path.append(state)
        steps += 1
    return path
