# Class
# Instance Attributes
from telnetlib import DO


class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says: Bark!')


myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

# Static Attributes
# 'legs' is a static variable. This is a static variable or class variable.
print(Dog.legs)
# You can reset value of the static variable
