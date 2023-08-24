# Programming challenge for comprehensions
import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# My first Solution


# Total length of the string
l = len(test_str)

# Total of number characters
nums = len([c for c in test_str if c.isnumeric()])

# Total of puctuation characters
punct = len([c for c in test_str if c in string.punctuation])

# Count unique letters
unique = "".join({c for c in test_str if c.isalpha})

# print the data
str_data = {
    "Length": l,
    "Digits": nums,
    "Punctuations": punct,
    "Unique Letters": unique,
    "Unique Count": len(unique)
}
print('First solution:\n')
pprint.pp(str_data)
print("")

# My second solution

str_data2 = {
    "Length": len(test_str),
    "Digits": len([b for b in test_str if b.isnumeric()]),
    "Punctuations": len([b for b in test_str if b in string.punctuation]),
    "Unique Letters": "".join({b for b in test_str if b.isalpha()}),
    "Unique Count": len({b for b in test_str if b.isalpha()})
}
print('Second solution:\n')
pprint.pp(str_data2)
