from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Set tracer to Off / none to set up the movement of each square together
# To use with time lib and screen.update()
screen.tracer(0)

snake = Snake()
food = Food()
score_track = Scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    # Get the tracer back on
    # Time sleep between each square move
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Get food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_track.score_track()

    # Game over if the snakes hits the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score_track.game_over()
        game_is_on = False

    # Game over if head hits the tail
    for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 8:
            game_is_on = False
            score_track.game_over()


screen.exitonclick()
