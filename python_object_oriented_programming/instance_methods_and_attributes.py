# Instance methods and attributes

# 1TODO: Create a basic class
class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        # 1TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute'

    # '1TODO': create instance methods
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# 1TODO: create some book instances
b1 = Book('Brave New World', 'Leo Tolstoy', 1225, 39.95)
b2 = Book('The Catcher in the Rye', 'JD Salinger', 234, 29.95)

# 1TODO: print the prince of book1
print(b1.getprice())

# 1TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())


# 1TODO: properites with double underscores are hidden by the interpereter
# print(b2.__secret) Outputs AttributeError: 'Book' object has no attribute '__secret'
print(b2._Book__secret)
# We are getting an error here because '__secret' is a property that cannot be seen outside the class.

# Name Mangeling ??
