from turtle import Turtle, Screen
import random
from colors import colors


def draw_shapes(no_of_sides):
    angle = 360 / no_of_sides
    turtle.color(random.choice(colors))
    for sides in range(0, no_of_sides):
        turtle.forward(50)
        turtle.right(angle)


turtle = Turtle()

turtle.shape("arrow")
turtle.color("green")
for shapes in range(3, 12):
    draw_shapes(shapes)

screen = Screen()
screen.exitonclick()
