# Programming challenge for Special Class Methods

# Challenge:
# Given a class that represents a Book with various properties such
# as title, author, pagecount, etc:
# 1) Implement the __repr__ and __str__ functions to output:
#   str:  "(title) by (author): (pagecount), (cover), (price)"
#   repr: "<Book:title:author:pages:cover:antique:genre:price>"
# 2) Implement the comparison methods to allow comparing books based
#   on pagecount.
# 3) Implement an enum that represents the type of the book cover. The
#   allowable cover types are "hard" and "paperback". Replace the existing
#   "Hard" and "paperback" strings with the enum.
# 4) Implement an "adjustedprice" computed attribute - books that are antiques
#   have a 10.00 surcharge on their price, Paperback books get a 2.00 discount
# 5) Successfully execute the sample code provided below.


# SOLUTION
from enum import Enum


# Implement the Hard/Paperback Enum
class CoverType(Enum):
    HARD = "Hard"
    PAPERBACK = "Paperback"


class Book():
    def __init__(self, title, author, pages, cover, antique, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover = CoverType(cover)
        self.antique = antique
        self.price = price

    # Implement the str and repr functions
    def __str__(self):
        return f"{self.title} by {self.author}: {self.pages}, {self.cover.value}, {self.price}"

    def __repr__(self):
        return f"<Book:{self.title}:{self.author}:{self.pages}:{self.cover.value}:{self.price}>"

    # Implement the adjustedprice attribute
    @property
    def adjustedprice(self):
        adj_price = self.price
        if self.antique:
            adj_price += 10.00
        if self.cover == CoverType.PAPERBACK:
            adj_price -= 2.00
        return adj_price

    # Implement comparisons <, >, <=, >=
    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __ge__(self, other):
        return self.pages >= other.pages


books = [
    Book("War and Peace", "Leo Tolstoy", 1225, "Hard", True, 29.95),
    Book("Brave New World", "Aldous Huxley", 311, "Paperback", True, 32.50),
    Book("Crime and Punishment", "Fyodor Dostoevsky", 492, "Hard", False, 19.75),
    Book("Moby Dick", "Herman Melville", 427, "Paperback", True, 22.95),
    Book("A Christmas Carol", "Charles Dickens", 66, "Hard", False, 31.95),
    Book("Animal Farm", "George Orwell", 130, "Paperback", False, 26.95),
    Book("Farenheit 451", "Ray Bradbury", 256, "Hard", True, 28.95),
    Book("Jane Eyre", "Charlotte Bronte", 536, "Paperback", False, 34.95)
]

# TEST CODE

# 1 - test the str and repr functions
print("--------------")
print(str(books[0]))
print(str(books[3]))
print(str(books[5]))
print()
print(repr(books[0]))
print(repr(books[3]))
print(repr(books[5]))
print("-------------\n")

# 2 - test the "adjustedprice" computed attribute
print("---------------")
for book in books:
    print(f"{book.title}: {book.adjustedprice:.2f}")
print("--------------\n")

# 3 - compare on pagecount
print(books[1] > books[2])
print(books[4] < books[6])
print(books[7] >= books[0])
print(books[3] <= books[4])
