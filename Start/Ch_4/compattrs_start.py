# Customize string representations of objects


class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # Use getattr to dynamically return a value
    def __getattr__(self, attr):

        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return f"{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError(f"{attr} is not valid")

    # Use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # Use dir to list the available properties
    def __dir__(self):
        return ("rgbcolor", "hexcolor")


# Create an instance of myColor
cls1 = MyColor()

# Print the value of a computed attribute
print(f"RGB color: {cls1.rgbcolor}")
print(f"Hex color: {cls1.hexcolor}")
print("")

# Set the value of a computed attribute
cls1.rgbcolor = (175, 225, 320)
print(f"RGB color after change: {cls1.rgbcolor}")
print(f"Hex color after change: {cls1.hexcolor}")
print("")

# Access a regular attribute
print(f"Regular attribute (Blue): {cls1.blue}")
print("")

# List the available attributes
print(f"Available attributes:  {dir(cls1)}")
