"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
import math


class Figure:
    def description(self):
        return "I am a figure"


class Circle(Figure):

    def __init__(self, radio):
        self.radio = radio

    def cal_area(self):
        return math.pi * (self.radio ** 2)

    def cal_perimeter(self):
        return 2 * math.pi * self.radio

    def description(self):
        return "I am a Circle"

    def __str__(self):
        return "Circle have a Area: {}, Perimeter: {}".format(self.cal_area(), self.cal_perimeter())


class Squeare(Figure):

    def __init__(self, side):
        self.side = side

    def cal_area(self):
        return self.side ** 2

    def cal_perimeter(self):
        return 4 * self.side

    def description(self):
        return "I am a Squeare"

    def __str__(self):
        return "Asqueare have a Area: {}, Perimeter: {}".format(self.cal_area(), self.cal_perimeter())


if __name__ == '__main__':
    A = Circle(2)
    print(A)
    print("------------------------------------------")
    B = Squeare(2)
    print(B)
