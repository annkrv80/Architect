from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.radius * 3.14


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Cube(Shape, Shape3D):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * (self.edge ** 2)

    def perimeter(self):
        return 12 * self.edge

    def volume(self):
        return self.edge ** 3


if __name__ == '__main__':
    a = Circle(3)
    print(a.area())
    print(a.perimeter())
    b = Rectangle(2, 5)
    print(b.area())
    print(b.perimeter())
    c = Cube(3)
    print(c.area())
    print(c.perimeter())
    print(c.volume())

