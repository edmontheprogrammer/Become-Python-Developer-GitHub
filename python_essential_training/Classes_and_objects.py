class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')


my_dog = Dog('Rover')
another_dog = Dog('Fluffy')
print(my_dog.speak())
print(another_dog.speak())
