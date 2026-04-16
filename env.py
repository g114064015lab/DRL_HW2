import numpy as np

class CliffWalkingEnv:
    def __init__(self, height=4, width=12):
        self.height = height
        self.width = width
        self.start_state = (height - 1, 0)
        self.goal_state = (height - 1, width - 1)
        self.cliff = [(height - 1, i) for i in range(1, width - 1)]
        self.state = self.start_state
        self.reset()

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action):
        """
        Actions: 0: Up, 1: Down, 2: Left, 3: Right
        """
        row, col = self.state
        if action == 0:  # Up
            row = max(row - 1, 0)
        elif action == 1:  # Down
            row = min(row + 1, self.height - 1)
        elif action == 2:  # Left
            col = max(col - 1, 0)
        elif action == 3:  # Right
            col = min(col + 1, self.width - 1)

        self.state = (row, col)
        
        if self.state in self.cliff:
            reward = -100
            self.state = self.start_state
            done = False  # RL typical implementation: cliff resets but doesn't end episode
        elif self.state == self.goal_state:
            reward = 0
            done = True
        else:
            reward = -1
            done = False
            
        return self.state, reward, done

    def get_num_states(self):
        return self.height * self.width

    def state_to_idx(self, state):
        return state[0] * self.width + state[1]
