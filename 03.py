"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.

----------------

=== Circulo ===
Perimetro:
Area:

=== Cuadrado ===
Perimetro:
Area:

"""
from math import pi


class Figura:
    
    def __init__(self):
        pass
   
    def perimetro(self):
        return print("No esta implementado el metodo")

    def area(self):
        return print("No esta implementado el metodo")


class Circulo(Figura):
    
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * pi * self.radio

    def area(self):
        return self.perimetro * self.radio / 2


class Cuadrado(Figura):
    
    def __init__(self, lado):
        self.lado = lado


cir = Circulo(5)
print("Valor circulo: {0}".format(str(cir.perimetro())))

cua = Cuadrado(5)
print(cua.perimetro())

print("hola")