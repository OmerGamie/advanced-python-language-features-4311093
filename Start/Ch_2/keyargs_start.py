# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def My_Function(
    name,
    age,
    *,
    suppress_exc=False
):
    pass

# Try to call the function without the keyword
# MyFunction(1, 2, True)


# Try to call the function with the keyword
My_Function(1, 2, suppress_exc=True)
