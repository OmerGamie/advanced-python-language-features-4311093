# Demonstrate how to use list comprehensions

# TODO: define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# TODO: Perform a mapping and filter function on a list
even_squared = list(map(lambda e: e**2,
                        filter(lambda e: e > 4 and e < 20, evens)))
print('Using mapping and filter: ', even_squared)

# TODO: Derive a new list of numbers fromm a given list using comprehension
squared_even = [e ** 2 for e in evens if 4 < e < 20]
print('Using list comprehension: ', squared_even)

# TODO: Limit the items operated on with a predicate condition
odd_squared = [e ** 2 for e in evens if 3 < e < 21]
print('Odds squared using list comprehesnion:\n', odd_squared)
