# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # Use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - fname:{self.fname}, lname: {self.lname}, age:{self.age}>"

    # Use str for a more human-readable string
    def __str__(self):
        return f"Person {self.fname} {self.lname} is {self.age}"

    # Convert the object into bytes
    def __bytes__(self):
        val = f"Person:{self.fname}:{self.lname}:{self.age}"
        return bytes(val.encode("utf-32"))


# Create a new Person object
cls1 = Person()

# Use different Python functions to convert it to a string
print(repr(cls1))
print("")

print(str(cls1))
print("")

print(f"Formatted: {cls1}")
print("")

print(bytes(cls1))
