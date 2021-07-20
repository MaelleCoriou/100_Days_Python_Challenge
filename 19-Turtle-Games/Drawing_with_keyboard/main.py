import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()


def move_forwards():
    """W key"""
    cursor.forward(10)


def move_backward():
    """S key"""
    cursor.backward(10)


def turn_left():
    """A key"""
    cursor.left(10)
    # new_heading = cursor.heading() + 10
    # cursor.setheading(new_heading)

def turn_right():
    """Key D"""
    # cursor.right(10)
    new_heading = cursor.heading() - 10
    cursor.setheading(new_heading)


def clear_screen():
    """D key"""
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()

screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=turn_left)
screen.onkey(key="D", fun=turn_right)

screen.exitonclick()
