from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for item in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            self.segments.append(new_turtle)
            new_turtle.goto(0 - 20 * item, 0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cord = self.segments[seg_num - 1].xcor()
            new_y_cord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x_cord, new_y_cord))
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)


