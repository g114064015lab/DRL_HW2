## ADDED Requirements

### Requirement: Interactive Parameters
The system SHALL provide a sidebar in Streamlit to configure:
- ε (exploration rate)
- α (learning rate)
- γ (discount factor)
- Number of episodes

#### Scenario: User adjusts Parameters
- **WHEN** user changes a slider or input value
- **THEN** the system SHALL update the training parameters for the next run.

### Requirement: Dashboard Layout
The system SHALL display the following in Streamlit:
- Comparison plot of total rewards.
- Visual grid for the Cliff Walking paths (Q-learning vs. SARSA).
- A theoretical comparison section (On-policy vs. Off-policy).

#### Scenario: View results
- **WHEN** the training is complete
- **THEN** the system SHALL render the reward curve and optimal paths on the main dashboard.
