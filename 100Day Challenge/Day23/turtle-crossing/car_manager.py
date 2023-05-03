import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_chance = randint(1,5)
        if random_chance == 1:
            car_new = Turtle()
            car_new.color(random.choice(COLORS))
            car_new.shape("square")
            car_new.penup()
            car_new.goto(280, randint(-250, 250))
            car_new.shapesize(1, 2)
            self.all_cars.append(car_new)

    def move_cars_forward(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
