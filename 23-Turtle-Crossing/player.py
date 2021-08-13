from turtle import Turtle
STARTING_POSITION = 0, -280
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # Turtle faces north
        self.setheading(90)
        self.got_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def got_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False















