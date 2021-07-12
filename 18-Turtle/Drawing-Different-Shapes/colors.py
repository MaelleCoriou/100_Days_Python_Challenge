import random


def color_shape():
    """Random colors provider format "r, g, b" """
    colors = []
    for color in range(3):
        colors.append(round(random.uniform(0, 1), 3))
    return colors
