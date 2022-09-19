# Built-in Function: isinstance(x, y)
# The isinstnace() method takes one object and one class information
# Output: Boolean representing whether or not the object is an instance of the class given by the class info.

class Car:
    pass


class Truck(Car):
    pass


c = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))
