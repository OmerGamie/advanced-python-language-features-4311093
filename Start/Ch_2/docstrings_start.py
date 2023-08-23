# Demonstrate how to write a Docstring


def points(twopointers, threepointers):
    """
    points(twopointers, threepointers) -> Cout points for a basketball game,
    it takes in the amount of 3-pointers scored and 2-pointers scored. It then
    calculates the final points using the formula and returns that value.
    Parameters:
    twopointers: 2-pointers scored
    threepointers: 3-pointers scored
    """
    return (twopointers * 2) + (threepointers * 3)


def string_combiner(*args, unique=False):
    """
    Combines a variable number of strings and numbers into a single string.
    Accepts a keyword-only argument 'unique'. 
       Parameters:
    *args: A variable number of arguments. Only strings and numbers will be combined.
    unique: A keyword-only argument. If True, the returned string will have no duplicate characters. Defaults to False.

    Returns:
    A combined string.

    Arguments of types other than string and int are ignored.
    """
    combined = ""
    for arg in args:
        if isinstance(arg, (str, int)):
            combined += str(arg)

    if unique:
        combined = "".join(sorted(set(combined), key=combined.index))

    return combined


print(points.__doc__)
