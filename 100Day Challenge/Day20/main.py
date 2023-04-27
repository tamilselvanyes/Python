import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

segments = []

for item in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")
    segments.append(new_turtle)
    new_turtle.goto(0 - 20 * item, 0)
    screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x_cord = segments[seg_num - 1].xcor()
        new_y_cord = segments[seg_num - 1].ycor()
        segments[seg_num].goto((new_x_cord,new_y_cord))
    segments[0].forward(20)

screen.exitonclick()
