from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def reset(self):
        for s in self.snakes:
            s.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        # end of the list segment
        self.add_segment(self.snakes[-1].position())

    def move(self):
        # Automatically move the snake, the tail follows the head
        # Range args : start / stop / step
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            # Move the last segment to the first segment
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Move up, but won't allow to move backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Move down, but won't allow to move backwards
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # Move right, but won't allow to move backwards
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # Move left, but won't allow to move backwards
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
