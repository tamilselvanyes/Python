from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.begin_fill()
        self.penup()
        self.pencolor("white")
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}", False, align="center", font=('Arial', 18, 'normal'))
