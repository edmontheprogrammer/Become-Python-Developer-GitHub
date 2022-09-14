# Inheritance
class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')

    def getLegs(self):
        return self._legs


class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')

    def wagTail(self):
        print('Vigorous wagging!')


dog = Chihuahua('Roxy')
print(dog.speak())
dog.wagTail()

myDog = Dog('Rover')
myDog.speak()
# Extending built-in classes

myList = list()  # 'list()' is a class


class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
UniqueList.append(1)
UniqueList.append(1)
UniqueList.append(2)

print(uniqueList)
