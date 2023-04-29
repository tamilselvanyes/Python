from turtle import Turtle


class Paddle():
    def __init__(self,position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.goto(position, 0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=3, stretch_len=0.5)

    def move_up(self):
        current_position = self.paddle.pos()
        x_pos_new = current_position[0]
        y_pos_new = current_position[1] + 20
        if y_pos_new < 280:
            self.paddle.goto(x_pos_new,y_pos_new)

    def move_down(self):
        current_position = self.paddle.pos()
        x_pos_new = current_position[0]
        y_pos_new = current_position[1] - 20
        if y_pos_new > -280:
            self.paddle.goto(x_pos_new, y_pos_new)



