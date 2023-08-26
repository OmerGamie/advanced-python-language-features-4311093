# Using pattern guards to restrict how matches are made

# define some geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height


# create a list of some shapes
shapes = [Circle(5), Square(4), Rectangle(4, 6),
          Square(7), Circle(9), Rectangle(2, 5), Rectangle(6, 6)]

# use pattern matching to process each shape
# Include pattern guards for more detailed processing
for shape in shapes:
    match shape:

        # Add a pattern guard for Circle
        case Circle(radius=r) if r >= 6:
            print(f"Large Circle with area {shape.getarea()}")
        case Circle(radius=r):
            print(f"Circle with area {shape.getarea()}")
        case Square():
            print(f"Square with area {shape.getarea()}")
        case Rectangle(width=w, height=h) if w == h:
            print(f"Square Rectangle with area {shape.getarea()}")
        case Rectangle():
            print(f"Rectangle with area {shape.getarea()}")
        case _:
            print(f"Unrecognized shape: {type(shape)}")
print("------------------")

# Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None, ]
numbers = [2, 30, 34, 33, 45, 76, 23, 22,
           10, 55, 606, 990, 488, 400]

for d in dataset:
    match d:
        case str() as s if s.isupper():
            print(f"{d}: Upper case string")
        case str():
            print(f"{d}: Not an upper case string")
        case bool():
            print(f"{d}: Boolean")
        case int():
            print(f"{d}: Integer")
        case _:
            print(f"{d}: Something else")
print("-------------------\n")

# pattern guards to detect odd numbers in a list
odd_numbers = []
for num in numbers:
    match num:
        case int() if num % 2 == 1:
            odd_numbers.append(num)
        case _:
            continue
print(f"Odd numbers in the list: {odd_numbers}")
