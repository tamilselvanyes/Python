from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for item in INITIAL_POSITION:
            self.add_segment(item)

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

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)
