from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("LightSalmon")

# Draw a square
# for sides in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw dashed line
for dash in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

# To keep at the bottom of the script
screen = Screen()
screen.exitonclick()
