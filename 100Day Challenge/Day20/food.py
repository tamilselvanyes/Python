from turtle import Turtle
from random import randint





class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed()
        self.refresh_food()

    def refresh_food(self):
        x_coordinate = randint(-280, 280)
        y_coordinate = randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)

