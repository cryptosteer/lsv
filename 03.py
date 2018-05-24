"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi

class Figura:

    name = "Ninguna"
    msg = ""

    def descripcion(self):
        return "Soy una figura"

    def area(self) -> float:
        pass

    def perimetro(self) -> float:
        pass

    def __str__(self):
        self.msg = "="*20+"\n"
        self.msg += "Caracteristicas del {}\n".format(self.name)
        self.msg += "\tArea -> {}\n".format(self.area())
        self.msg += "\tPerimetro -> {}\n".format(self.perimetro())
        self.msg += "\tDescripcion -> {}\n".format(self.descripcion())
        return self.msg

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

    def __str__(self):
        return super(Circulo, self).__str__() + "\tRadio -> {}".format(self.radio)

class Cuadrado(Figura):

    def __init__(self, l):
        self.lado_dim = l
        self.name = "Cuadrado"

    def area(self):
        return self.lado_dim ** 2

    def perimetro(self):
        return 4 * self.lado_dim

    def __str__(self):
        return super(Cuadrado, self).__str__() + "\tDimension de los lados -> {0}".format(self.lado_dim)


if __name__ == "__main__":
    my_circle = Circulo(4.90)
    print(my_circle)

    my_square = Cuadrado(4)
    print(my_square)

