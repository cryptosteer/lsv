"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
<<<<<<< HEAD
import math


class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self):
        return "Soy una figura"


class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return math.pi*(self.radio**2)

    def perimetro(self):
        return 2*math.pi*self.radio

    def __str__(self):
        return "Soy un circulo"


class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return self.lado*self.lado

    def perimetro(self):
        return self.lado*4

    def __str__(self):
        return "Soy un cuadrado"

# c=Circulo(int(input("Ingrese el radio deseado: ")))
circulo=Circulo(8)
print("El area del circulo es: ", circulo.area())
print("El perimetro del circulo es: ", circulo.perimetro())
print(circulo)
cuadrado=Cuadrado(2)
print("--------------------------------")
print("El area del cuadrado es: ", cuadrado.area())
print("El perimetro del cuadrado es: ", cuadrado.perimetro())
print(cuadrado)
=======

>>>>>>> c66552e9af1004537b049c53377a56bc6a20cd1d
