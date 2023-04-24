from turtle import Turtle, Screen
import random
from colors import colors

directions = [0, 90, 180, 270]
widths = [5, 6, 7, 8, 9, 10]
turtle = Turtle()
turtle.shape("arrow")
turtle.color("green")

for _ in range(0, 100):
    turtle.forward(30)
    turtle.speed("fastest")
    turtle.width(random.choice(widths))
    turtle.color(random.choice(colors))
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
