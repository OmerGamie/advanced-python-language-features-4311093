# Demonstrate how to use set comprehensions

# define a list of temperature data points
ctemps = [2, 5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29, 32]

# Build a set of unique Fahrenheit temperatures
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
print('Temprature wit duplicate values:\n', ftemps1)

ftemps2 = {(t * 9/5) + 32 for t in ctemps}
print('Temperature with unique values:\n', ftemps2)

# Build a set from an input source
pangram = "Swiftly, the chestnut fox vaulted over the sluggish hound"
chars = {c.upper() for c in pangram if not c.isspace() and c != ','}
print('My pangram set: ', chars)
