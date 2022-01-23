from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_2 = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self,):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(x=0, y=350)
        self.write(f"Score = {self.score}", False, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT_2)