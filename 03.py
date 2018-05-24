"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calarea(self):
        return math.pi * (self.radio ** 2)

    def calpermiter(self):
        return 2 * math.pi * self.radio


if __name__ == '__main__':
    A = Circulo(2)

    print("The area is :", A.calarea())
    print("THe perimeter is:", A.calpermiter())
