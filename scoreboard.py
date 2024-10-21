from turtle import Turtle

# Constant for the font style and size used in the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1 at the start of the game
        self.hideturtle()  # Hide the turtle object, as we only want to display text
        self.penup()  # Lift the pen to avoid drawing lines when moving the turtle
        self.goto(-280, 250)  # Position the scoreboard near the top left of the screen
        self.update_scoreboard()  # Display the initial scoreboard

    # Method to display or update the current level on the screen
    def update_scoreboard(self):
        self.clear()  # Clear the previous text
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    # Method to increase the level when the player completes a level
    def increase_level(self):
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the displayed level

    # Method to display the "Game Over" message when the player loses
    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)  # Display "GAME OVER" in the center
