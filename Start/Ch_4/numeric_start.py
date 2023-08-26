# Example file for Advanced Python: Language Features by Joe Marini
# give objects number-like behavior


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x:{self.x},y:{self.y}>"

    # Implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


# Declare some points
p1 = Point(20, 40)
p2 = Point(50, 70)
print(f"P1: {p1}, P2: {p2} \n")

# Add two points
p3 = p1 + p2
print(f"Addition: {p3} \n")

# Subtract two points
p4 = p2 - p1
print(f"Subtraction: {p4} \n")

# Perform in-place operations
p1 += p2
print(f"In-place addition: {p1} \n")

p1 -= p2
print(f"In_place subtraction: {p1}")
