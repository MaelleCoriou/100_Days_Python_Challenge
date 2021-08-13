import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Car crossing")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # game over if player hits a car
    for x in car.cars:
        if x.distance(player) < 20:
            game_is_on = False

    if player.finish_line():
        player.got_to_start()
        car.level_up()
        score.score_track()
        score.update_scoreboard()

score.game_over()

screen.exitonclick()