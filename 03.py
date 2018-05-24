"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi
class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * pi * self.radio

    def area(self):
        return self.perimetro * self.radio / 2

cir = Circulo(5)

print(cir.perimetro())

class Cuadrado(Circulo):

    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * pi * self.radio

    def area(self):
        return self.perimetro * self.radio / 2

cua = Cuadrado(5)


print(cua.perimetro())
