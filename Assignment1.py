# Exercise: Write a loop that prints out every character of your name
def printName(str):
    for char in str:
        print(char)

printName("Lidsyda")

# Turtle Graphics with loops

import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed(0) # Set the speed of the turtle

# Function to move the turtle
def walk_turtle(steps):
    for _ in range(steps):
    # Move forward a fixed distance
        angle = random.randint(0, 360)
        t.forward(20)

     # Determine a random angle between -180 and 180 degrees to turn
        t.right(angle)

# Number of steps the turtle will take
num_steps = 100
walk_turtle(num_steps)

# Close the turtle graphics window on click
turtle.done()
