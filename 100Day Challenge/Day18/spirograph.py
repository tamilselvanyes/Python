from turtle import Turtle, Screen
import turtle as t
import random

directions = [0, 90, 180, 270]
turtle = Turtle()
turtle.shape("arrow")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for item in range(0, 50):
    turtle.circle(100)
    turtle.speed("fastest")
    turtle.color(random_color())
    turtle.left(item)

screen = Screen()
screen.exitonclick()
