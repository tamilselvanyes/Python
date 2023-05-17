from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        print("Init called")
        with open("/Users/tamilselvan/Desktop/data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        print("Updating score",self.high_score)
        self.write(f"Score:  {self.score} High Score:{self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            print("Updating the high score")
            self.high_score = self.score
            with open("../../../../data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


