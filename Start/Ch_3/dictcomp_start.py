# Demonstrate how to use dictionary comprehensions

# TODO: define a list of temperature values
ctemps = [0, 6, 12, 34, 100]

# TODO: Use a comprehension to build a dictionary
temp_dict = {t: (t*9/5) + 32 for t in ctemps if t < 100}
print('Temperature: ', temp_dict)
print('Temperature for value (6): ', temp_dict[6])

# TODO: Merge two dictionaries with a comprehension
team1 = {"Omer": 24, "Mona": 18, "Sammy": 58, "Bara": 7}
team2 = {"Basil": 12, "Ahmed": 88, "Ali": 4}
merged_team = {k: v for team in (team1, team2) for k, v in team.items()}
print('Merged Team: ', merged_team)
