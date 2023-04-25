from turtle import Turtle, Screen
import turtle as t
import random

turtle = Turtle()
turtle.shape("arrow")
t.colormode(255)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        turtle.circle(100)
        turtle.color(random_color())
        turtle.setheading(turtle.heading() + gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
