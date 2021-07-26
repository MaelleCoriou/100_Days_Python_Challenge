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


# --------- CLASS --------- #
# Create a class
class Users:
    pass


# create object with the class
user_1 = Users()

# create attribute with object
user_1.id = "001"
user_1.name = "Maëlle"

# For second user
user_2 = Users()
user_2.id = "002"
user_2.name = "Jack"

print(user_1.name)


# def __init__ used to initialize attributes
# Avoid repeating new objects to create attributes

class UsersWithInit:

    # create parameters to use as attributes
    # The attributes are the things the object has
    def __init__(self, user_id, user_name):
        self.name = user_name
        self.id = user_id
        # default set up
        self.followers = 0
        self.following = 0

    # The methods are the things the object does
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = UsersWithInit("001", "Maëlle")
user_2 = UsersWithInit("002", "Jack")

print(user_1.name)
print(user_1.id)
print(user_1.followers)

# user 1 follows user 2
user_1.follow(user_2)
print("user_1 =", user_1.followers)
print("user_1 =", user_1.following)
print("user_2 =", user_2.followers)
print("user_2 =", user_2.followers)



