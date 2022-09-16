# Interfaces
# An interface is kinda like a promise or a contract that a class makes to provide certain kind
# of behavior that it will have at the end of its creation.

from abc import ABC, abstractmethod

# Note 1; the 'toJSON' method does not provide any implmentation itself, we are just using the
# 'pass' keyword which is a placeholder to make the class run without giving us error for not
# adding anything in the method body. It just provides the name of the


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# Note 1: This class is inheriting from GraphicShape and JSONify class.
# Note 2: 'JSONify' class is an abstract class, so this class must implement the '@abstractmethod' or methods from the
# 'JSONify'.
# Note 3: GraphicShape is a concerete class or a normal class, so this class does not have to implement any
#  methods from 'GraphicShape'. It can overwrite methods from 'GraphicShape', but it's required to do so.


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius)

    def toJSON(self):
        return f"{{\" circle\" : {str(self.calcArea())}  }}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
