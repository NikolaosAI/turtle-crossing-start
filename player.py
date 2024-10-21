from turtle import Turtle

# Constants for the player's start position, movement, and finish line
STARTING_POSITION = (0, -280)  # Player starts at the bottom center of the screen
MOVE_DISTANCE = 10  # Distance the player moves with each "up" key press
FINISH_LINE_Y = 280  # Y-coordinate representing the finish line at the top of the screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the player's shape to a turtle
        self.penup()  # Disable drawing lines when the player moves
        self.color("black")  # Set the turtle color to black
        self.go_to_start()  # Start the player at the bottom of the screen
        self.setheading(90)  # Set the turtle's heading to face upwards (north)

    # Move the player upwards by a set distance
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Reset the player to the starting position at the bottom of the screen
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Check if the player has reached the finish line at the top of the screen
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y  # Return True if the player is past the finish line
