from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(-280, 260)
        self.update_score()
        self.color("black")
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, )

    def increase_score(self):
        self.score += 1
        self.update_score()