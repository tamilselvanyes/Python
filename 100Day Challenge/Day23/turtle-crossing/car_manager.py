import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = Turtle()
        self.car.color(random.choice(COLORS))
        self.car.shape("square")
        self.car.penup()
        self.car.goto(280, randint(-240, 240))
        self.car.shapesize(1, 2)

    def move_cars_forward(self):
        self.car.goto(self.car.xcor() - MOVE_INCREMENT, self.car.ycor())
