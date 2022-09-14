import math


class Orientation:
    def __init__(self, x_pos, y_pos, degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = self.getUnitVectorFromDegrees(degrees)

    @staticmethod
    def getUnitVectorFromDegrees(self, degrees):
        radiants = (degrees / 180) * math.pi
        return math.sin(math.radians), -math.cos(math.radians)

    def getNextPos(self):
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir


myOrientation = Orientation(5, 5, 75)
myOrientation.getNextPos()


# Decorators
# Decorators defines special attributes or information about functions
# so that Python knows how to handle it.
