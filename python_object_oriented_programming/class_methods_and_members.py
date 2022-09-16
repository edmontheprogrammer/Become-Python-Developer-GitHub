# Using class-level and static methods

class Book:
    # 1TODO: Properties defined at the class level are shared by all
    # instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')

    # 1TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # 1TODO: create a class method

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # 1TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods recieve a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# 1TODO: access the class attribute
print("Book types: ", Book.getbooktypes())

# 1TODO: create some book instances
b1 = Book('Title 1', 'HARDCOVER')
b2 = Book('Title 2', 'PAPERBACK')

# 1TODO: use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
