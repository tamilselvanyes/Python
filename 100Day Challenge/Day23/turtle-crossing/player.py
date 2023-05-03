from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor() , self.ycor() - MOVE_DISTANCE)

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())


