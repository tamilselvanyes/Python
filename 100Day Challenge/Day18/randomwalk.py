from turtle import Turtle, Screen
import turtle as t
import random
from colors import colors

directions = [0, 90, 180, 270]
widths = [5, 6, 7, 8, 9, 10]
turtle = Turtle()
turtle.shape("arrow")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


for _ in range(0, 100):
    turtle.forward(30)
    turtle.speed("fastest")
    turtle.color(random_color())
    turtle.width(random.choice(widths))
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
