import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_managers = []


game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    car_manager_new = CarManager()
    car_managers.append(car_manager_new)
    for car_manager in car_managers:
        car_manager.move_cars_forward()


screen.exitonclick()