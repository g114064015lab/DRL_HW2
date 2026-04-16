## ADDED Requirements

### Requirement: Gridworld Layout
The system SHALL implement a 4x12 gridworld.
- The bottom-left cell (row 3, col 0) is the START state.
- The bottom-right cell (row 3, col 11) is the GOAL state.
- Cells between START and GOAL (row 3, cols 1-10) are the CLIFF.

#### Scenario: Agent reaches the Cliff
- **WHEN** the agent enters any cell designated as CLIFF
- **THEN** the system SHALL assign a reward of -100 and reset the agent's position to START.

### Requirement: Standard Movement
The system SHALL allow four discrete actions: UP, DOWN, LEFT, RIGHT.

#### Scenario: Agent moves into a standard cell
- **WHEN** the agent takes a valid non-cliff, non-goal move
- **THEN** the system SHALL assign a reward of -1 and update the agent's position.

#### Scenario: Agent moves into the Goal
- **WHEN** the agent enters the GOAL cell
- **THEN** the system SHALL assign a reward of 0 (or -1 depending on convention, but episode ends) and terminate the episode.
