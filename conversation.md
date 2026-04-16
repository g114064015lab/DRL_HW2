# Conversation Log: DRL Homework 2 - Cliff Walking Comparison

This document records the development process and decision-making for the Reinforcement Learning Homework 2: Q-Learning vs SARSA.

## 📅 Session Metadata
- **Project**: Cliff Walking Gridworld Comparison
- **Date**: 2026-04-16
- **Developer**: Antigravity (AI Assistant) & User

## 💬 Key Discussion Points

### 1. Initialization & Workflow Setup
- Initialized **OpenSpec** for change management.
- Implemented a numbering rule for changes (e.g., `c01-`).
- Created `startup.sh` and `ending.sh` for automated environment setup and project wrap-up.

### 2. Requirement Analysis
- Defined the Cliff Walking environment (4x12 grid, -100 cliff penalty, ε=0.1, α=0.5, γ=0.99).
- Specified the need for comparing **Q-Learning** (Off-policy) and **SARSA** (On-policy).
- Identified the requirement for a **Streamlit** dashboard for interactive visualization.

### 3. Implementation Phases
- **Environment**: Developed `env.py` with custom grid logic.
- **Agents**: Developed `agents.py` with TD-learning update rules.
- **Experiment Engine**: Implemented `experiment.py` with multi-run averaging (e.g., 10-50 runs) to reduce variance and match theoretical benchmarks.
- **Frontend**: Created `app.py` using Streamlit, featuring dynamic parameter control and side-by-side performance comparisons.

### 4. Deployment & Troubleshooting
- Configured GitHub repository: `https://github.com/g114064015lab/DRL_HW2`.
- Resolved `ModuleNotFoundError` on Streamlit Cloud by optimizing `requirements.txt` and triggering rebuilds.
- Fixed UI visibility issues (text color) in Streamlit metrics and theory sections using custom CSS.

### 5. Final Polish
- Added the live demo URL to `README.md`.
- Finalized parameters: Episodes 500+, α=0.5, γ=0.99.

## 🛠️ Resulting Codebase
- [app.py](app.py)
- [env.py](env.py)
- [agents.py](agents.py)
- [experiment.py](experiment.py)
- [visualization.py](visualization.py)
- [README.md](README.md)
- [requirements.txt](requirements.txt)
- [conversation.md](conversation.md)

---
*End of Conversation Log.*
