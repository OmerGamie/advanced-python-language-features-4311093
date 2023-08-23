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


print(points.__doc__)
