"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro
que devuelva el perímetro del circulo.
"""
import math


class Shape:

    PI = round(math.pi)

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return 'I\'m figure'


class Square(Shape):

    def __init__(self, base):
        self.base = base

    def area(self):
        return pow(self.base, 2)

    def perimeter(self):
        return self.base * 4

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(base={self.base})'

    def __str__(self):
        return f'{super(Square, self).__str__()} \n' \
               f'El area del circulo es: {self.area()} ' \
               f'y su perimetro es {self.perimeter()}'


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self, **kwargs):
        return self.PI * pow(self.radius, 2)

    def perimeter(self):
        return self.PI * self.radius * 2

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(radius={self.radius})'

    def __str__(self):
        return f'{super(Circle, self).__str__()} \n' \
               f'El area del circulo es: {self.area()} ' \
               f'y su perimetro es {self.perimeter()}'


circle = Circle(radius=5)
square = Square(base=5)

print(circle)
print(repr(circle))
print()
print(square)
print(repr(square))
