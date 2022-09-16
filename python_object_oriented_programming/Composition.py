# Using Composition
# Composition is the idea of creating complex objects from simple objects.
# When using composition, we build objects out of other objets, and this model is more of a has relationship.
# Book = ['Title', 'Price', 'Author' ] ---> Author = ['First Name', 'Last Name']
# For example, we can say the Book object has an 'author' object, which contains information about the author.
# This is possible because the 'Book' is an object made up of multiple objects
# ('Title' object, 'Price' object and 'Author' object).
#  and 'Author' is one of those objects. Instead of creating and listing all the author information directly
# within the book class hierarchy. We create a separate class specifically for the 'author' information.
# Then we create an instance of the 'Author' class inside the 'Book' book. That's why we are able to say
# " The 'Book' has 'Author' ".
# This type of model lets us extract distnct ideas, and put them into their own classes.

# Note 1; Remeber that you can combine inheritance and composition together.


# Note 2; we created a book, 'Book' class, that has an author, 'Author' class, assoicated with it.
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

# Creating a class named 'Author' that extract the author information into its own class


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapetr 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())
