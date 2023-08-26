# Demonstrate how to define enumerations using the Enum base class
from enum import Enum, unique, auto


# TODO: enums have human-readable values and types


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    BLUE_DELECIOUS = 5
    PEAR = auto()


# Enums have name and value properties
print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))
print("")

print(Fruit.APPLE.name, Fruit.APPLE.value)
print("")

# Print the auto-generated value
print(Fruit.PEAR.value)
print("")

# Enums are hashable - can be used as keys
my_fruits = {}
my_fruits[Fruit.BANANA] = "Here's your Banana Juice!"
print(my_fruits[Fruit.BANANA])
