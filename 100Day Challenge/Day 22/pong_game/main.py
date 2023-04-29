from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(800, 600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer()

player_one = Paddle((-380,0))
player_two = Paddle((370,0))
ball = Ball()

screen.listen()
screen.onkey(player_one.move_up, 'w')
screen.onkey(player_one.move_down, 's')
screen.onkey(player_two.move_up, 'Up')
screen.onkey(player_two.move_down, 'Down')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_forward()

    if ball.pos()[1] > 270 or ball.pos()[1] < -270:
        ball.change_direction()
screen.exitonclick()