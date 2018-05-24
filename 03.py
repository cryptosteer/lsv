"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi

class Figura:

    name = "Ninguna"

    def descripcion(self):
        return "Soy una figura"

    def area(self) -> float:
        pass

    def perimetro(self) -> float:
        pass

    def show(self):
        print("="*20)
        print("Caracteristicas del {}".format(self.name))
        print("\tArea -> {}".format(self.area()))
        print("\tPerimetro -> {}".format(self.perimetro()))
        print("\tDescripcion -> {}".format(self.descripcion()))

class Circulo(Figura):

    def __init__(self, rd):
        self.radio = rd
        self.name = "Circulo"

    def area(self):
        return pi * (self.radio ** 2)

    def perimetro(self):
        return 2*pi*self.radio

    def show(self):
        super().show()
        print("\tRadio -> {}".format(self.radio))


class Cuadrado(Figura):

    def __init__(self, l):
        self.lado_dim = l
        self.name = "Cuadrado"

    def area(self):
        return self.lado_dim ** 2

    def perimetro(self):
        return 4 * self.lado_dim

    def show(self):
        super().show()
        print("\tDimension de los lados -> {}".format(self.lado_dim))


if __name__ == "__main__":
    my_circle = Circulo(4.90)
    my_circle.show()

    my_square = Cuadrado(4)
    my_square.show()

