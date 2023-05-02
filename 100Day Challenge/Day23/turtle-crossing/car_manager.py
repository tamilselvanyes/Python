from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        for car in COLORS:
            turtle_new = Turtle()
            turtle_new.color(car)
            turtle_new.shape("square")
            turtle_new.shapesize(1, 2)
            turtle_new.goto(turtle_new.xcor() + MOVE_INCREMENT, turtle_new.ycor())
            self.cars.append(turtle_new)

