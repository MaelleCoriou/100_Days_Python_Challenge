class Figure:

    def __init__(self, n_sides, n_move, turtle_object):
        # Get track of sides number
        self.sides = n_sides
        # Get track of move distance
        self.move = n_move
        # Get track of angle size
        self.angle_size = 0
        # Turtle Type
        self.turtle = turtle_object

    def draw_shape(self):
        """To draw shapes parameters n_sides: numbers of sides
        n_move: distance move, n_angle: angle in int
        turtle_type: turtle object (shape)"""
        for n in range(self.sides):
            self.turtle.forward(self.move)
            self.turtle.left(self.angle_size)

    def size_shape(self):
        """Calculates the parameters to draw multiple shapes.
        parameters: n_sides: number of sides, n_move: distance move,
        returns the appropriate angle to draw"""
        self.sides += 1
        self.angle_size = 360 / self.sides

