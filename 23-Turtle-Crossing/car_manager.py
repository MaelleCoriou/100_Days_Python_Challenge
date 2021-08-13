from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(COLORS[random.randint(0, 5)])
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            y_position = random.randint(-295, 295)
            x_position = 300
            car.setposition(x_position, y_position)
            self.cars.append(car)

    def move(self):
        for x in self.cars:
            x.setheading(180)
            x.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT






