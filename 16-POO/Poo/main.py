# import turtle
#
# timmy = turtle.Turtle()
#
# print(timmy)
#
# from turtle import Turtle, Screen
#
# # New object
# timmy = Turtle()
# print(timmy)
# # Call methods with attributes
# timmy.shape("turtle")
# timmy.color("green")
# timmy.shapesize(5, 5, 12)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

# creating object table with class Prettytable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# Text align left
# table.align["Pokemon Name"] = "l"
table.align = "l"
print(table)

