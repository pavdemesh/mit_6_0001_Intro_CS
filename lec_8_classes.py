# from abc import ABC, abstractmethod
#
#
# class Coordinate(object):
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self, other):
#         print(f"self.x is {self.x} and other.x is {other.x}")
#         x_dist = (self.x - other.x) ** 2
#         y_dist = (self.y - other.y) ** 2
#         return (x_dist + y_dist) ** 0.5
#
#     def __str__(self):
#         return f"<{self.x},{self.y}>"
#
#
# point_1 = Coordinate(3, 4)
# point_2 = Coordinate(0, 0)
#
# print(point_1.distance(point_2))
# print(Coordinate.distance(point_1, point_2))
# print(point_1)
#
# point_1.size = "tiny"
# print(point_1.size)
#
#
# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         print('Animal moves')
#
#
# class Cat(Animal):
#     def move(self):
#         # super().move()
#         print('Cat moves')
#
#
# c = Cat()
# c.move()

class Test:
    def __init__(self):
        self.__name = "Peter"

    def get_name(self):
        return self.__name


c = Test()
print(c.get_name())
