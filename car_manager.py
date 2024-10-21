from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Possible colors for cars
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 10  # Speed increase when the player levels up

class CarManager:
    def __init__(self):
        self.all_cars = []  # List to keep track of all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Set the initial speed of the cars

    # Creates a new car with a random chance (1 out of 6 times per loop)
    def create_car(self):
        random_chance = random.randint(1, 6)  # Randomly decide if a car is created (about 1 in 6 loops)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new turtle object for the car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Shape the car as a rectangle
            new_car.penup()  # Prevent the car from drawing lines as it moves
            new_car.color(random.choice(COLORS))  # Choose a random color from the COLORS list
            random_y = random.randint(-250, 250)  # Generate a random Y-position within the screen bounds
            new_car.goto(300, random_y)  # Start the car at the right edge of the screen
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    # Moves all cars across the screen from right to left
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car by the current speed
            # Remove the car if it goes off-screen (left side)
            if car.xcor() < -320:
                car.hideturtle()  # Hide the car to improve performance
                self.all_cars.remove(car)  # Remove the car from the list

    # Increases the car speed when the player levels up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # Increase the speed of all cars
