
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self, dimensions):
        pass

    @abstractmethod
    def perimeter(self, dimensions):
        pass


class Square(Shape):

    def area(self, side):
        return side ** 2

    def perimeter(self, side):
        return 4 * side


class Rectangle(Shape):

    def area(self, side: list):
        return side[0] * side[1]

    def perimeter(self, side):
        return 2 * side[0] * side[1]


# sq = Square()
# print(sq.area(2))
#
# rct = Rectangle()
# print(rct.perimeter([23, 90]))

# sh = Shape()
# print(sh.area(None))