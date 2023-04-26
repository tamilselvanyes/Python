from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def handle_w():
    turtle.forward(10)


def handle_s():
    turtle.backward(10)


def handle_d():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def handle_a():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def handle_c():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=handle_w)
screen.onkey(key="s", fun=handle_s)
screen.onkey(key="a", fun=handle_a)
screen.onkey(key="d", fun=handle_d)
screen.onkey(key="c", fun=handle_c)
screen.exitonclick()
