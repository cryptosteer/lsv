"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área
 y otro que devuelva el perímetro del circulo.
"""
import math


class Figura:

    def descripcion(self):
        return ("Soy una figura")


class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        a =  math.pi * math.sqrt(self.radio)
        return a

    def perimetro(self):
        p = math.pi * self.radio * 2
        return p

    def descripcion(self):
        return ("Soy un Circulo")


class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        a = math.sqrt(self.lado)
        return a

    def perimetro(self):
     p = 4 * self.lado
     return p

    def descripcion(self):
        return ("Soy un Cuadrado")


c=Circulo(10)
print("El area del circulo es: ",c.area())
print("El perimetro del circulo es: ",c.perimetro())
print(c.descripcion())


cu = Cuadrado(5)
print("El area del cuadrado es: ", cu.area())
print("El perimetro del cuadrado es: ", cu.perimetro())
print(cu.descripcion())

