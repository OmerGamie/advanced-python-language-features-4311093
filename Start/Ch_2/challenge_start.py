# Challenge solution file for Advanced Functions

# Challenge:
# Write a function that performs the following actions:
# 1: accepts a variable number of strings and numbers. Other types ignored
# 2: accepts a keyword-only argument to return a unique-only result
# 3: combines all the arguments into a single string
# 4: returns a string containing all arguments combined as one string
# 5: Has a docstring that explains how it works
# If the unique-only argument is True (default False), then the result
# combined string will not contain any duplicate characters


def string_combiner(*args, unique=False):
    result = ""

    # YOUR CODE HERE

    return result


# test code:
print(string_combiner.__doc__)
output = string_combiner("This", "is", 1, "test", "string!", unique=False)
print(output)
output = string_combiner("This", "is", 1, "test", "string!", unique=True)
print(output)
output = string_combiner("This", "is", 1, True, "string!", unique=False)
print(output)
output = string_combiner("This", "is", [1, 2], "string!", unique=False)
print(output)
