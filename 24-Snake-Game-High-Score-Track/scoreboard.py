from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.clear()
        self.update_scoreboard()

    def read(self):
        with open("score.txt", mode="r") as f:
            score_track = f.read()
        return score_track

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Updates the score to the highest score
        if self.score > self.high_score:
            self.high_score = self.score
            self.record_high_score()
        self.score = 0
        self.update_scoreboard()

    def score_track(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def record_high_score(self):
        with open("score.txt", mode="w") as f:
            f.write(str(self.score))







