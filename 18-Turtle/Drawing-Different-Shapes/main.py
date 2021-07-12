from turtle import Turtle, Screen
from Drawing import Figure
from colors import color_shape

shape = Turtle()
drawing = Figure(2, 50, shape)


for turns in range(10):
    shape.color(color_shape())
    drawing.size_shape()
    drawing.draw_shape()


# To keep at the bottom of the script
screen = Screen()
screen.exitonclick()
