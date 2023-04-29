from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.title("PONG")
screen.bgcolor("black")

player_one = Paddle(-380)
player_two = Paddle(370)

screen.listen()
screen.onkey(player_one.move_up, 'Up')
screen.onkey(player_one.move_down, 'Down')


screen.exitonclick()