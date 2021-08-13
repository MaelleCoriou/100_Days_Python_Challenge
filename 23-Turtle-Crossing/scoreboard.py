from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"level {self.score}", False, align="left", font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"level {self.score}", False, align="left", font=FONT)

    def game_over(self):
        self.setposition(0 , 0)
        self.write(f"Game Over", False, align="center", font=FONT)

    def score_track(self):
        self.score += 1
