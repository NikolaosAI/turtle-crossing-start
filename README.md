 # Turtle Crossing Game

Welcome to the **Turtle Crossing Game**! This game is inspired by the classic "Frogger" game, where the player controls a turtle to cross a busy road without getting hit by cars. The goal is to reach the top of the screen while avoiding cars that move at increasing speeds as you level up.

## Game Overview

- **Player**: Controls a turtle that moves upward across the screen using the "Up" arrow key.
- **Cars**: Move horizontally across the screen from right to left. The number and speed of cars increase with each level.
- **Objective**: Reach the top of the screen without colliding with any cars to advance to the next level.

## Features

- Turtle player moves with keyboard input.
- Randomly generated cars with various colors.
- Increasing difficulty as the game progresses (cars move faster with each level).
- A scoreboard to track the player's current level.
- Game Over display when the player collides with a car.

## How to Play

1. Use the "Up" arrow key to move the turtle upward.
2. Avoid the cars crossing the screen by carefully timing your movements.
3. When the turtle reaches the top of the screen, it resets to the starting position, and the car speed increases as you level up.
4. The game ends if the turtle collides with any car.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NikolaosAI/turtle-crossing-game.git

2. Navigate to the project directory:

bash

cd turtle-crossing-game

3. Install the required dependencies. The game uses the built-in turtle module, which is available by default in Python.

4. Run the game:

bash

    python main.py

File Structure

    main.py: The main game loop and setup for the game.
    player.py: Defines the Player class, representing the turtle that the player controls.
    car_manager.py: Defines the CarManager class, responsible for creating and moving cars.
    scoreboard.py: Defines the Scoreboard class, which tracks the player's current level and handles the game over message.


Future Improvements

    Adding sound effects for movement and collisions.
    Increasing the difficulty by adding more obstacles or different car patterns.
    Supporting additional movement keys (left, right) to allow for more complex movements.

Contributing

Feel free to fork this repository and make your own changes! If you'd like to contribute, open an issue or submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
