# Using multiple inheritance
# Pyhon is an OOP that allows multiple inheritance. Unlike Java you can only inherit from one class at a time.
# This means one class can get attributes and methods from multiple parent classes at the same time.

class A:
    def __init__(self):
        super().__init__()
        self.foo = 'foo'
        self.name = 'Class A'


class B:
    def __init__(self):
        super().__init__()
        self.bar = 'bar'
        self.name = 'Class B'


# Note 1; Class 'C' is inheriting from class 'A' and 'B'. Class 'A' and 'B' are parent classes and class 'C'
# is a child class or subclass.
class C(A, B):
    def __init__(self):
        super().__init__()

        # this function is printing two attributes that defined inside the parent class, 'A' and 'B',
        # We are able to do this through inheritance.
    def showprops(self):
        print(self.foo)
        print(self.bar)
        # method resolution gives us the name attribute defined in class 'A' because it's listed first in the
        # parenthsis of class 'C'\'s declartion. If you switch the order of inheritance and put class B first.
        # then the name attribute defined inside class 'B' will be printed.
        print(self.name)


c = C()
c.showprops()
# '__mro__' gives us the method resolution.
print(C.__mro__)
