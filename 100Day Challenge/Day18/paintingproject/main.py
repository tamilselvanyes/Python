import colorgram
from turtle import Turtle, Screen
import random
import turtle as t

# colors = colorgram.extract('spot-painting.jpg', 50)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     formatted_color = (r, g, b)
#     rgb_colors.append(formatted_color)
#
# print(rgb_colors)

turtle = Turtle()
turtle.penup()
t.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()

dot_colors = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191),
              (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93),
              (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42),
              (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45),
              (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23),
              (219, 206, 8), (181, 186, 213), (46, 72, 57), (168, 201, 212), (100, 137, 144)]


for row in range(20):
    for column in range(10):
        turtle.color(random.choice(dot_colors))
        turtle.dot(8)
        if column < 9:
            turtle.forward(32)

    if row % 2 == 0:
        turtle.setheading(90)
        turtle.forward(32)
        turtle.setheading(180)
    else:
        turtle.setheading(90)
        turtle.forward(32)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()