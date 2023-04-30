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
    ball_x_pos = ball.pos()[0]
    ball_y_pos = ball.pos()[1]
    print(ball.distance(player_one), "1 distance")
    print(ball.distance(player_two), "2 distance")
    if ball_y_pos > 270 or ball_y_pos < -270:
        ball.change_y_direction()
    if ball.distance(player_one) < 30 or ball.distance(player_two) < 30:
        ball.change_x_direction()

    if ball_x_pos > 380:
        game_is_on = False

    if ball_x_pos < -380:
        game_is_on = False

screen.exitonclick()