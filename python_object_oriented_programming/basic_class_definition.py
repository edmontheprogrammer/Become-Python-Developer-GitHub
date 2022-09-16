# Basic class definitions

# 1TODO: Create a basic class
class Book():
    def __init__(self, title):
        self.title = title


# 1TODO: create instances of the class
b1 = Book('Brave New World')
b2 = Book('War and Peace')

# 1TODO: print the class and property
print(b1)  # prints the object of the  Book class, you'll need to add the
# string method into the Book class if you want to see human
# readable data???
print(b1.title)
