from turtle import Turtle, Screen
import random


def color_shape():
    """Random colors provider format "r, g, b" """
    colors = []
    for color in range(3):
        colors.append(round(random.uniform(0, 1), 3))
    return colors


cursor = Turtle()
cursor.speed("fastest")
cursor.hideturtle()


def draw_recursive(gap):
    """gap set up : space between each circle"""
    for circle in range(int(360 / gap)):
        cursor.color(color_shape())
        cursor.circle(150)
        # setheading gets the current position adding gap to go forward
        # cursor.setheading(cursor.heading() + gap)
        cursor.left(gap)


draw_recursive(5)

screen = Screen()
screen.exitonclick()
