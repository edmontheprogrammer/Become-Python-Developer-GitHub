# Pyton magic methods are methods that Python automatically associates with class definitions.
# Customize object behavior and integrate with the language
# Define how objects are represented as strings
# Control access to attribute values, both for get and set
# Build in comparison and quality testing capabilites
# Allow objects to be called like functions

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # 1TODO: use the __str__ method to return a string repersenation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # 1TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

    # 1TODO: the __eq__ method checks for equality between two objects
    # This is the method you need to implement if you want to compare objects
    # in Python. In addition, you must compare the attributes one by one to each
    # other in order to see the full object comparisons.
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # 1TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")

        return self.price >= value.price

    # 1TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")

        return self.price < value.price


# Creating two book objects and printing them out.
b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book(" To Kill a Mockingbird", "Harper Lee", 24.95)

# Part B: 1TODO: Check for equality
# print(b1 == b3)
# print(b1 == b2)
# # print(b1 == 42) # Value error cannot compare a book to something that's not a book

# # 1TODO: check for greater and lesser value
# print(b2 >= b1)
# print(b2 < b1)

# 1TODO: Now we can sort them too
books = [b1, b3, b4]
books.sort()
print([book.title for book in books])


# Part A: 1TODO : Check for equality
# Outputs 'False' because 'b1' and 'b2' are two separate objects in memory
# print(b1 == b3)
# that are independent of each other. And when we are comparing 'b1' to 'b3' using '=='
# we are actually comparing the memory addresses of 'b1' to 'b3', we are not comparing the
# the values or contents of these variables.
# If you want to compare two objects to each other in Python, you need to implement the
# '__eq__' and compare the class 'attributes' or 'object attributes' ??? to each other one by one
#

# printing 'b1' and 'b2' without the '__str__' method outputs the memory address of the objects
# in memory.
# print(b1)
# print(b2)

# print(str(b1))
# print(repr(b2))
