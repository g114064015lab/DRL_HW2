## Context

The project involves comparing two classic Temporal Difference (TD) reinforcement learning algorithms: Q-learning and SARSA. The environment is a 4x12 Gridworld with a "cliff" that penalizes the agent and resets its position. The primary challenge is to demonstrate how Q-learning follows the optimal (but risky) path while SARSA follows a safer (more conservative) path due to its on-policy nature.

## Goals / Non-Goals

**Goals:**
- Implement a reusable Cliff Walking Gridworld environment.
- Implement modular Q-learning and SARSA agents.
- Develop a Streamlit application for interactive visualization.
- Generate performance graphs comparing cumulative rewards.
- Output path visualizations for each agent.

**Non-Goals:**
- Using external gym libraries (implementing from scratch for better control and less overhead).
- Implementing deep reinforcement learning (Deep Q-Networks).
- Optimizing for large-scale state spaces.

## Decisions

- **State Representation**: The grid will be represented as a 2D coordinate system (row, col) but flattened into a single integer `row * 12 + col` for Q-table indexing.
- **Data Structures**: `numpy` will be used for the Q-table (48x4 array) to ensure fast vector operations during updates.
- **Frontend Architecture**: `Streamlit` will be used to host the app. The simulation will run either on-demand or show cached results for faster responsiveness.
- **Visuals**: `streamlit.pyplot` for graphs and `streamlit.table` or a custom HTML/CSS grid for path visualization.

## Risks / Trade-offs

- **[Risk] Convergence Issues**: If learning rate α or discount factor γ are poorly tuned, the agents might not converge in 500 episodes.
- **Mitigation**: Use the standard values provided (α=0.1, γ=0.9) and verify against known Sutton & Barto results.
- **[Trade-off] Scratch Implementation vs. Gym**: Implementing the environment from scratch adds more code but eliminates versioning issues with `gym` or `gymnasium`.
