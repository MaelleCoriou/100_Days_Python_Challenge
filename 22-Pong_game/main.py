from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen set up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Paddle set up
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

# Move paddles Up and Down
screen.listen()
screen.onkey(fun=left_paddle.up, key="s")
screen.onkey(fun=left_paddle.down, key="w")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # rebound with wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.rebound_y()

    # rebound with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.rebound_x()

    # reset position when ball's doesn't touch the paddle and bounces to the opposite side
    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.l_point()

screen.exitonclick()
