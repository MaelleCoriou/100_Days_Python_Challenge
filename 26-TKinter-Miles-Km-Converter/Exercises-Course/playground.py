# *args enable unlimited arguments, can be called differently as long as it begins with an *
# *args is saved as tuple, a specific arg can be called in the function print(args[1])

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def add2(*args):
    print(type(args))
    print(args[2])
    return sum(args)


print(add(3, 6, 8, 80))
print(add2(3, 6, 8, 80))


# Key words arguments kwargs
# **kwargs returns a dictionary
def calculate(n, **kwargs):
    # for key, value in kwargs:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add=5, multiply=3))

class car:
    def __init__(self, **kw):
        self.brand = kw["brand"]
        self.model = kw["model"]

# All kw need to be entered
my_car = car(brand="Peugeot", model="3006")
print(my_car.model)
print(my_car.brand)


# Use .get() methode so it won't crash if only 1 arg is given
class car_optional:
    def __init__(self, **kw):
        self.brand = kw.get("brand")
        self.model = kw.get("model")

my_car = car_optional(brand="Peugeot")
print(my_car.model)
print(my_car.brand)
