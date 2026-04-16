import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from env import CliffWalkingEnv
from experiment import run_experiment, get_optimal_path
from visualization import plot_rewards, visualize_grid_path

st.set_page_config(page_title="RL Cliff Walking Comparison", layout="wide")

# --- UI Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    [data-testid="stMetricValue"] {
        color: #000000 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
    }
    .theory-box {
        background-color: #e9ecef;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #000000 !important;
    }
    .theory-box h3, .theory-box p, .theory-box b {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏔️ Cliff Walking: Q-Learning vs SARSA")
st.write("An interactive comparison of Off-Policy and On-Policy reinforcement learning.")

# --- Sidebar Parameters ---
with st.sidebar:
    st.header("⚙️ Training Parameters")
    episodes = st.slider("Episodes", 500, 2000, 500, step=100)
    alpha = st.slider("Learning Rate (α)", 0.01, 1.0, 0.5)
    gamma = st.slider("Discount Factor (γ)", 0.5, 1.0, 0.99)
    epsilon = st.slider("Exploration Rate (ε)", 0.01, 0.5, 0.1)
    num_runs = st.slider("Number of Runs to Average", 1, 50, 10)
    
    run_btn = st.button("🚀 Run Experiment", use_container_width=True)

# --- Theoretical Background ---
tab1, tab2, tab3 = st.tabs(["📊 Performance", "🗺️ Learned Paths", "📖 Theory & Analysis"])

if run_btn:
    with st.spinner("Training agents..."):
        q_agent, q_rewards = run_experiment('q_learning', episodes, alpha, gamma, epsilon, num_runs)
        s_agent, s_rewards = run_experiment('sarsa', episodes, alpha, gamma, epsilon, num_runs)
        
        env = CliffWalkingEnv()
        q_path = get_optimal_path(q_agent, env)
        s_path = get_optimal_path(s_agent, env)

    with tab1:
        st.subheader("Learning Curves")
        fig = plot_rewards(q_rewards, s_rewards)
        st.pyplot(fig)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Q-Learning Avg Reward (Last 100)", f"{np.mean(q_rewards[-100:]):.2f}")
        with col2:
            st.metric("SARSA Avg Reward (Last 100)", f"{np.mean(s_rewards[-100:]):.2f}")

    with tab2:
        st.subheader("Optimal Trajectories")
        
        def display_grid(path, title):
            grid = visualize_grid_path(path)
            fig, ax = plt.subplots(figsize=(10, 3))
            im = ax.imshow(grid, cmap='viridis')
            ax.set_title(title)
            # Annotate Grid
            for r in range(4):
                for c in range(12):
                    label = ""
                    if r == 3 and 0 < c < 11: label = "CO"
                    elif r == 3 and c == 0: label = "S"
                    elif r == 3 and c == 11: label = "G"
                    
                    if (r, c) in path:
                        ax.text(c, r, "●", ha='center', va='center', color='white', fontweight='bold')
                    else:
                        ax.text(c, r, label, ha='center', va='center', color='gray')
            st.pyplot(fig)

        display_grid(q_path, "Q-Learning Strategy (Optimal but Risky)")
        st.caption("Q-Learning tends to choose the path right next to the cliff because it is the shortest path to the goal.")
        
        display_grid(s_path, "SARSA Strategy (Safe & Conservative)")
        st.caption("SARSA chooses a safer path because it accounts for the potential penalty of falling off the cliff during exploration.")

with tab3:
    st.markdown("""
    <div class="theory-box">
    <h3>Q-Learning (Off-Policy)</h3>
    <p>Q-learning learns the action-value function Q(s, a) by assuming the <b>best possible</b> next action is taken, regardless of what the agent actually does. This allows it to learn the optimal path, even if it falls into the cliff frequently during training due to exploration.</p>
    <hr>
    <h3>SARSA (On-Policy)</h3>
    <p>SARSA (State-Action-Reward-State-Action) updates its values based on the action <b>actually taken</b> by the agent. Since the agent explores randomly 10% of the time, it "knows" that walking near the cliff is dangerous. Thus, it learns a safer, more distant path to avoid accidental falls.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Observation**: Notice how the SARSA performance curve is generally smoother and higher during training because it avoids the -100 penalty more effectively than Q-learning.")

if not run_btn:
    st.info("Configure the parameters in the sidebar and click 'Run Experiment' to begin.")
