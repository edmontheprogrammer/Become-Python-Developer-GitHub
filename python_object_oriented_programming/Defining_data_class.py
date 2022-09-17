# Defining a data class
# Using data classes to represent data objects
# Post init function ???


from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.author} "


# create some instnaces
b1 = Book("War and peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and peace", "Leo Tolstoy", 1225, 39.95)

# access fields
# print(b1.title)
# print(b2.author)

# # 1TODO: print the book itself - dataclasses implement __repr__
# print(b1)

# # 1TODO: comparins the two dataclasses - they implement __eq__
# print(b1 == b3)

# 1TODO Change some fields
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())
