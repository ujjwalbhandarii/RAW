
# abc --> module
# abstractmethod --> decorator
from abc import ABCMeta, abstractmethod

# this is abstract base class


class Shape(metaclass=ABCMeta):  # can also write " ABC "
    @abstractmethod
    def printarea(self):
        return 0


class Rectange(Shape):
    type = "Reactange"
    sides = 4

    def __init__(self) -> None:
        self.length = 2
        self.breadth = 2

    def printarea(self):
        return self.length * self.breadth


ujjwal = Rectange()

print(ujjwal.printarea())


# note --> we can make objects of abstact base class
