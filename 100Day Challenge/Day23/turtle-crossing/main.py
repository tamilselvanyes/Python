import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars_forward()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
        if player.ycor() > FINISH_LINE_Y:
            player.move_to_starting_point()
            car_manager.level_up()
            score.increase_score()


screen.exitonclick()