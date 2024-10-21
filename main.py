import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen for the game
screen = Screen()
screen.setup(width=600, height=600)  # Set the window size to 600x600 pixels
screen.title("Turtle Crossing")  # Set the title of the game window
screen.tracer(0)  # Turn off automatic animation, allows manual control for smoother movement

# Create game objects: player, car manager, and scoreboard
player = Player()  # The turtle controlled by the player
car_manager = CarManager()  # Manages the movement and creation of cars
scoreboard = Scoreboard()  # Displays the current level and game over message

# Set up keyboard controls
screen.listen()  # Start listening for keyboard events

# Bind the "Up" arrow key to move the player upwards
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True  # Boolean to control when the game is running
while game_is_on:
    time.sleep(0.1)  # Pause the game for 0.1 seconds to control speed of the loop
    screen.update()  # Refresh the screen with updated positions

    # Create a new car with a random chance and move all cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If a car is within 20 pixels of the player, it's a collision
            game_is_on = False  # Stop the game
            scoreboard.game_over()  # Display the "GAME OVER" message

    # Check if the player successfully crossed to the top
    if player.is_at_finish_line():
        player.go_to_start()  # Move the player back to the starting position
        car_manager.level_up()  # Increase the speed of the cars
        scoreboard.increase_level()  # Increase the player's level on the scoreboard

# Keep the game window open until clicked
screen.exitonclick()
