# Abstract Base Classes
# An Abstract Base Class is a generic class that allows subclasses to implemenet from it.
# It enfoces constraints that subclasses have to implement.
# Abstract Base class is just an idea.
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod

# Note 1; In Python, you make declare a class to be an abstract base class by making that
# class inherit from the 'ABC' class. 'ABC' class is a built-in class in Python
# Note 2; Then I'm going to use the abstract method decorator, '@abstractmethod' , to indicate
# that the 'calcArea' function is an abstract method. So this tells Python that there' no
# implementation in the base class. And each subclass has to override this method, 'calcArea()'.


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

# g = GraphicShape() # Outputs an error because you cannot create an instance of abstract classes
# and abstract classes are meant to be abstract.
# 'TypeError: Can't instantiate abstract class GraphicShape with abstract method calcArea'


# Outputs error; TypeError: Can't instaintate abstract class Circle wth abstract
c = Circle(10)
# method 'calcArea()'. This error happened because the subclass 'Circle' is inheriting from
# the abstrac class 'GraphicShape' but 'Circle' did not implement the abstract method in
# its body. All subclasses that uses abstract classes must inherit from the abstract classes and
# implement all the methods that marked as abstract method. Therefore, to fix this error, simply
# implmenet the 'calcArea()' method in the subclass, 'Circle'.
print(c.calcArea())
s = Square(12)
print(s.calcArea())
