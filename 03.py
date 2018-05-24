"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""


class figura:
    def descripcion(self):
        return "soy una figura"


class Circulo (figura):

    def __init__(self, rad):
        self.radio=rad
        self.pi=3.14
    def descripcion(self):
        return "soy un circulo"

    def area(self):
        return (self.pi*(self.radio*self.radio))

    def perimetro(self):
        return (2*(self.radio*self.pi))


circulo1=Circulo(20)
print(circulo1.descripcion())
print("el area del circulo es: ", circulo1.area())
print("el perimetro del circulo es :", circulo1.perimetro())

class cuadrado (figura):
    def __init__(self, lad):
        self.lado=lad
    def descripcion(self):
        return "soy un cuadrado"
    def area(self):
        return self.lado*self.lado

    def perimetro(self):
        return self.lado*4


cuadrado1=cuadrado(10)
print(cuadrado1.descripcion())
print("el area del cuadrado es: ", cuadrado1.area())
print("el perimetro del cuadrado es: ", cuadrado1.perimetro())
