from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_direction = 1
        self.y_direction = 1

    def move_forward(self):
        self.goto(self.xcor() + (self.x_direction * 20), self.ycor() + (self.y_direction * 20))

    def change_y_direction(self):
        self.y_direction *= -1

    def change_x_direction(self):
        self.x_direction *= -1
