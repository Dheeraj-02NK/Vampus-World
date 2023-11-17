# Vampus World Game

## Objective

Navigate an agent through a grid-based world to find gold while avoiding the vampus.

## Gameplay

- **Grid:** The game is played on a grid, where the agent, vampus, and gold are positioned.

- **Agent:** Represented by a blue oval, the agent is controlled by arrow buttons to move in the up, down, left, or right directions.

- **Vampus:** Represented by a red icon, the vampus is an obstacle. If the agent comes into proximity, a "Smoke! Vampus is nearby" warning is displayed.

- **Gold:** Represented by a yellow icon, the gold is the target. When the agent reaches the gold, a "Congratulations! You found the gold" message is displayed.

- **Feedback:** The game provides feedback on the agent's proximity to the vampus and outcomes (e.g., finding gold or getting caught by the vampus).

- **Buttons:** Arrow buttons allow the player to move the agent in the corresponding direction.

- **Game Over:** The game ends when the agent finds the gold or is caught by the vampus, and an appropriate message is displayed.

## Implementation Details

### Code Structure

- **VampusWorld:** Represents the game world with the agent, vampus, and gold positions. Handles movements and feedback.

- **VampusGUI:** Implements the graphical user interface using Tkinter. Displays the grid, agent, vampus, and gold. Manages buttons and feedback display.

### Visualization

- The GUI displays a grid, where the agent and obstacles move.

- Images (icons) are used for the agent, vampus, and gold.

- Buttons provide a user interface to control the agent's movements.

### Game Logic

- The game checks for proximity to the vampus, displays feedback, and updates the game state.

- The player wins by reaching the gold or loses by getting caught by the vampus.

### Interactivity

- The player interacts with the game by clicking arrow buttons to move the agent.

### Extensibility

- The code is extensible, allowing for multiple vampus and gold positions.

## How to Play

1. Run the script.
2. Use arrow buttons to navigate the blue agent.
3. Try to find the gold while avoiding the red vampus.
4. The game ends when the agent finds the gold or is caught by the vampus.

Have fun exploring the Vampus World!
