## ADDED Requirements

### Requirement: Training Loop
The system SHALL execute 500 episodes for each algorithm.

#### Scenario: Completion of training
- **WHEN** 500 episodes are finished
- **THEN** the system SHALL provide the cumulative rewards per episode for plotting.

### Requirement: Performance Plotting
The system SHALL generate a plot comparing Q-learning and SARSA.

#### Scenario: Plot generation
- **WHEN** training data is available
- **THEN** the system SHALL save an image file showing the episodes on the X-axis and total reward on the Y-axis.
