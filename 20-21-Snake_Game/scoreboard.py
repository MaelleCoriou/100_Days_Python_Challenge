from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)

    def score_track(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




