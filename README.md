# Cliff Walking: Q-Learning vs SARSA

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://drlhw2-gmfyrfappaingv6wuj72s2k.streamlit.app/)

A Reinforcement Learning project focused on implementing and comparing two classic Temporal Difference algorithms: **Q-Learning (Off-policy)** and **SARSA (On-policy)** using the Cliff Walking Gridworld environment.

## 🏔️ Project Overview

This project simulates a 4x12 gridworld where an agent must navigate from a Start position (bottom-left) to a Goal position (bottom-right). Between the start and goal lies a "Cliff." Falling into the cliff results in a heavy penalty (-100) and resets the agent to the starting position.

The goal is to analyze the behavioral differences:
- **Q-Learning** typically finds the optimal path along the edge of the cliff but is risky during training.
- **SARSA** learns a safer, more conservative path to avoid the cliff during exploration.

## 🚀 Interactive Dashboard

The project includes a **Streamlit** application for interactive exploration.

### Features:
- **Dynamic Hyperparameters**: Adjust ε, α, γ, and the number of episodes in real-time.
- **Live Comparison Plot**: Visualize cumulative rewards per episode.
- **Path Visualization**: Compare the learned trajectories of both agents on the grid.
- **Theoretical Documentation**: In-depth explanation of the underlying algorithm differences.

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.10+
- `pip` or `conda`

### Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/g114064015lab/DRL_HW2.git
   cd DRL_HW2
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📂 File Structure
- `app.py`: Main Streamlit application.
- `env.py`: Cliff Walking environment definition.
- `agents.py`: Q-Learning and SARSA agent logic.
- `experiment.py`: Training engine.
- `visualization.py`: Graphing and grid rendering utilities.
- `openspec/`: OpenSpec project management and specifications.

## 🎓 Theory Comparison
- **Q-Learning**: Updates the Q-value based on the maximum possible future reward (Greedy), allowing it to ignore exploration noise during learning.
- **SARSA**: Updates based on the actual next action taken (including exploration), making it aware of the danger of falling when exploration is active.

---
*Developed as part of the DRL Course Homework.*
