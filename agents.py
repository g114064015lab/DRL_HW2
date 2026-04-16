import numpy as np
import random

class Agent:
    def __init__(self, num_states, num_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = np.zeros((num_states, num_actions))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_actions = num_actions

    def choose_action(self, state_idx):
        if random.random() < self.epsilon:
            return random.randint(0, self.num_actions - 1)
        else:
            return np.argmax(self.q_table[state_idx])

class QLearningAgent(Agent):
    def update(self, state, action, reward, next_state, done):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + (0 if done else self.gamma * self.q_table[next_state][best_next_action])
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error

class SarsaAgent(Agent):
    def update(self, state, action, reward, next_state, next_action, done):
        td_target = reward + (0 if done else self.gamma * self.q_table[next_state][next_action])
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error
