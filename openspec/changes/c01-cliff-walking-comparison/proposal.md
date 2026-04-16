## Why

The goal of this project is to implement and compare two fundamental reinforcement learning algorithms, Q-learning and SARSA, within the "Cliff Walking" Gridworld environment. This comparison will highlight the differences between off-policy (Q-learning) and on-policy (SARSA) methods in terms of learning safety, convergence speed, and strategy selection.

## What Changes

- Implementation of a 4x12 Cliff Walking Gridworld environment.
- Implementation of the Q-learning (off-policy) algorithm.
- Implementation of the SARSA (on-policy) algorithm.
- Execution of 500 training episodes for both algorithms with ε-greedy exploration (ε=0.1).
- Development of a Streamlit dashboard to visualize results, trajectories, and parameters.
- Generation of comparative analysis plots (Rewards vs. Episodes).
- Visualization of final paths taken by both agents.

## Capabilities

### New Capabilities
- `cliff-walking-sim`: Implementation of the Gridworld environment with cliff penalties (-100) and step costs (-1).
- `rl-agents`: Implementation of Q-learning and SARSA agents sharing a common interface.
- `evaluation-suite`: Tools for training, measuring total rewards, and visualizing learned policies/paths.
- `streamlit-frontend`: Interactive web dashboard for configuring parameters and viewing real-time training progress and path visualizations.

## Impact

- New codebase for reinforcement learning experimentation.
- High-quality visualization assets for the homework report.
- Comparative data documenting the "conservative" vs. "optimal" path behaviors.
