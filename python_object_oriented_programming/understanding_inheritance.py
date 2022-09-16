# Understanding Class Inheritance
# Note 1; Remember that Python is one of the programming languages that allows mutliple inheritance.
# But Java only allows a single inheritance or you can only inherit from once class at a time
# in Java

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Perodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        # Note 1: 'super().__init__' method is initializing the values for 'title'
        #          and 'price' in the line below and we are initialzing the 'author' and
        # 'pages' like we normally do.
        super().__init__(title, price)
        # self.title = title
        # self.price = price
        self.author = author
        self.pages = pages


class Magazine(Perodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        # self.title = title
        # self.price = price
        # self.period = period
        # self.publisher = publisher


class Newspaper(Perodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        # self.title = title
        # self.price = price
        # self.period = period
        # self.publisher = publisher


b1 = Book('Brave New World', 'Aldous Huxley', 311, 29.0)
n1 = Newspaper('NY Times', 'New York Times Company', 6.0, 'Daily')
m1 = Magazine('Scientific American', 'Springer Nature', 5.99, 'Monthly')

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
