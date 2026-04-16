## 1. Environment Implementation

- [x] 1.1 Create `env.py` with a `CliffWalkingEnv` class.
- [x] 1.2 Implement state transition logic and cliff penalty (-100).
- [x] 1.3 Add coordinate-to-state index conversion logic.

## 2. RL Agents Implementation

- [x] 2.1 Create `agents.py` defining a base `Agent` class and `QLearningAgent` subclass.
- [x] 2.2 Implement the off-policy Q-Learning update rule.
- [x] 2.3 Implement the `SarsaAgent` subclass with the on-policy updates.
- [x] 2.4 Implement ε-greedy action selection for both agents.

## 3. Training and Evaluation

- [x] 3.1 Create `experiment.py` to handle the training loop (500 episodes).
- [x] 3.2 Collect total rewards per episode for both Q-Learning and SARSA.
- [x] 3.3 Save the trained Q-tables for path visualization.

## 4. Analysis and Reporting

- [x] 4.1 Create `visualization.py` using `matplotlib` to plot reward curves.
- [x] 4.2 Implement path visualization to show the differences in strategy (cliff-side vs. safe path).

## 5. Streamlit Deployment

- [x] 5.1 Create `app.py` for Streamlit.
- [x] 5.2 Add widgets for hyperparameters ( ε, α, γ).
- [x] 5.3 Integrate training and visualization into the Streamlit UI.
- [x] 5.4 Add a summary of theoretical differences in the app.
