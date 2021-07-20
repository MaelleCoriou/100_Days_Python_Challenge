from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_game_on = False
all_turtles = []

for i in range(len(colors)):
    y = -100
    y += (i * 40)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_turtle} turtle is the winner.")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
