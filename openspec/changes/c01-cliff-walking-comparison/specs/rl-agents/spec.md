## ADDED Requirements

### Requirement: Q-learning Implementation
The system SHALL implement the Q-learning algorithm.
- Update rule: Q(s,a) = Q(s,a) + α [R + γ max_a' Q(s',a') - Q(s,a)]

#### Scenario: Q-learning update
- **WHEN** an action is taken and the next state is observed
- **THEN** the system SHALL update the Q-table using the maximum Q-value of the next state (off-policy).

### Requirement: SARSA Implementation
The system SHALL implement the SARSA algorithm.
- Update rule: Q(s,a) = Q(s,a) + α [R + γ Q(s',a') - Q(s,a)]

#### Scenario: SARSA update
- **WHEN** an action is taken and the next action from the next state is observed
- **THEN** the system SHALL update the Q-table using the Q-value of the action actually chosen by the policy (on-policy).

### Requirement: Exploration Strategy
The system SHALL use ε-greedy exploration.

#### Scenario: ε-greedy action selection
- **WHEN** choosing an action
- **THEN** with probability ε, the agent SHALL choose a random action, and with probability 1-ε, it SHALL choose the action with the highest Q-value.
