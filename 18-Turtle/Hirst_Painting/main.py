import colorgram
import turtle
import random

# Path to the jpg file
img = "image.jpg"


def color_panel(image):
    """ Extracts colors from an image and return randomly a colour
     arg image: path to the jpg file"""
    color_list = colorgram.extract(image, 100)

    color_palette = []

    for i in range(len(color_list)):
        color_palette.append((color_list[i].rgb.r, color_list[i].rgb.g, color_list[i].rgb.b))

    # Delete background colors
    del color_palette[0:3]

    return random.choice(color_palette)


def draw_dots(dot_size, gap_size, color):
    """Draws dot line with random color"""
    cursor.color(color)
    cursor.pendown()
    cursor.dot(dot_size)
    cursor.penup()
    cursor.forward(gap_size)


def cursor_start(x_position, y_position):
    """Set the position of the cursor, x and y position args"""
    cursor.penup()
    cursor.goto(x_position, y_position)


cursor = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

cursor.hideturtle()
cursor.speed("fastest")

# Set turtle position
x_pos = -595
y_pos = -280

for draw in range(20):
    cursor_start(x_pos, y_pos)
    # Move the cursor to the upper line
    y_pos += 30
    for line in range(43):
        draw_dots(15, 28, color_panel(img))

screen.exitonclick()
