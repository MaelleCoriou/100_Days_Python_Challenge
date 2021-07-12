import random
from turtle import Turtle, Screen


## ------- RANDOM WALK TURTLE WITH MULTICOLOR DRAW ---------- ##


def color_shape():
    """Random colors provider format "r, g, b" """
    colors = []
    for color in range(3):
        colors.append(round(random.uniform(0, 1), 3))
    return colors


screen = Screen()
cursor = Turtle()

direction = [0, 90, 180, 270]

cursor.speed("fastest")
cursor.hideturtle()
#screen.screensize(100, 100)
cursor.pensize(10)

for i in range(400):
    cursor.color(color_shape())
    random_walk = random.choice(direction)
    cursor.forward(40)
    cursor.setheading(random_walk)

screen.exitonclick()
