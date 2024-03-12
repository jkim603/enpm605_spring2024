from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Usage
# shape = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
circle = Circle(5)
# print(circle.area())  # 78.5
# print(circle.perimeter())  # 31.4
