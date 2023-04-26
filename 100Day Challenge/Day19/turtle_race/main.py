from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

screen.setup(width=500, height=400)
user_input = screen.textinput("BET YOUR FAVORITE", "Choose the color of the turtle \n"
                                                   "red,orange,yellow,green,blue,indigo,violet?"
                              )

all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, -150 + (turtle_index * 50))
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won!!, The {winning_color} turtle won the race")
            else:
                print(f"You've lost!!, The {winning_color} turtle won the race")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
