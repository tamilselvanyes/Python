from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(60)

    def move_forward(self):
        self.forward(20)

    def change_direction(self):
        self.setheading(360 - self.heading())
