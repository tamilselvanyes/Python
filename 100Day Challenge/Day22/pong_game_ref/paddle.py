from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=0.5)

    def move_up(self):
        current_position = self.pos()
        x_pos_new = current_position[0]
        y_pos_new = current_position[1] + 20
        if y_pos_new < 280:
            self.goto(x_pos_new,y_pos_new)

    def move_down(self):
        current_position = self.pos()
        x_pos_new = current_position[0]
        y_pos_new = current_position[1] - 20
        if y_pos_new > -280:
            self.goto(x_pos_new, y_pos_new)



