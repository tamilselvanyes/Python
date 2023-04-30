from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.player_one_score = 0
        self.player_two_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-10, 280)
        self.write("Scores", move=False, align='left', font=('Arial', 14, 'normal'))
        self.goto(0, 260)
        self.write(f"{self.player_one_score} - {self.player_two_score}", move=False, align='left',
                   font=('Arial', 14, 'normal'))
