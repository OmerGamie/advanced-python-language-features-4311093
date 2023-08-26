# Objects pattern matching example - matches against object types
from math import pi

# define some geometric shapes


class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height


# Create a list of some shapes
shapes = [Circle(5), Square(4), Rectangle(4, 6),
          Square(7), Circle(9), Rectangle(2, 5), Triangle(3, 7)]

# Use pattern matching to process each shape
for shape in shapes:
    match shape:
        case Circle():
            print(f"Circle with area {shape.get_area()}")
        case Square():
            print(f"Square with area {shape.get_area()}")
        case Rectangle():
            print(f"Rectangle with area {shape.get_area()}")
        case Triangle():
            print(f"Triangle with area {shape.get_area()}")
        case _:
            print(f"Unrecognized shape: type({shape})")
