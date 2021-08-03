from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_position = 10
        self.x_position = 10
        self.ball_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_position
        new_x = self.xcor() + self.x_position
        self.goto(new_x, new_y)

    def rebound_y(self):
        self.y_position *= -1

    def rebound_x(self):
        self.x_position *= -1
        # increase speed
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.rebound_x()

