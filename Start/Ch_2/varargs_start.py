# Demonstrate the use of lambda functions

# TODO: Define a function that takes variable arguments
def addition(*nums):
    result = 0
    for num in nums:
        result += num
    return result


# TODO: Pass different arguments
print(addition(5, 10, 7, 22))
print(addition(19, 1, 4))

# TODO: Pass an existing list and use the unpacker
my_list = [5, 10, 7, 22, 19, 1, 4]
print(addition(*my_list))
