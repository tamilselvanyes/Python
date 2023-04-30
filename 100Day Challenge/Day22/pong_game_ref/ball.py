from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_direction = 20
        self.y_direction = 20

    def move_forward(self):
        self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)

    def change_y_direction(self):
        self.y_direction *= -1

    def change_x_direction(self):
        if self.speed() < 10:
            self.speed(self.speed() + 1)
        self.x_direction *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.speed(2)
        self.change_x_direction()
