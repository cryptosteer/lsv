"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi

class Circulo:

    def __init__(self, rd):
        self.radio = rd

    def Area(self):
        return pi*(self.radio**2)

    def Perimetro(self):
        return 2*pi*self.radio


if __name__ == "__main__":
    my_circle = Circulo(4.90)
    print("Caracteristicas del circulo")
    print("\tRadio -> {}".format(my_circle.radio))
    print("\tArea -> {}".format(my_circle.Area()))
    print("\tPerimetro -> {}".format(my_circle.Perimetro()))