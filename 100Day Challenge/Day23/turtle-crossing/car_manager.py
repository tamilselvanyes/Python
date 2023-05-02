from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INITAL_CAR_POSITION = [(280,-240), (280,-160), (280,-80), (280,0), (280,80), (280,160)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        for index,car in enumerate(COLORS):
            turtle_new = Turtle()
            turtle_new.color(car)
            turtle_new.shape("square")
            turtle_new.shapesize(1, 2)
            turtle_new.goto(INITAL_CAR_POSITION[index])
            self.cars.append(turtle_new)

    def move_cars_forward(self):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT,car.ycor())