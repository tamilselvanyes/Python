from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.update_score()
        self.color("black")
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT,align="center")