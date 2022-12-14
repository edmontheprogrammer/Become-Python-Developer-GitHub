# Callable Objects

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # reprsentation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # 1TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstoy", 38.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# 1TODO: call the object as if it were a function
print(b1)
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
