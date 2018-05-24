"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
class Figure:
    def area(self):
        pass
    def permiter(self):
        pass
    def __str__(self):
        return 'Soy una Figura!'


class Circulo(Figure):
    PI = 3.1416
    def __init__(self, radio=0.0):
        self.radio = radio

    def area(self):
        return round(self.PI*(self.radio**2))

    def perimeter(self):
        return round(2*self.PI*self.radio)

    def __str__(self):
        rep = "Circulo de radio: ".format(self.radio)+"\n"
        rep += "Area: {0} y perimetro {1}".format(self.area(), self.perimeter())
        return rep

class Rectangle(Figure):
    def __init__(self, base=0.0, height=0.0):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def permiter(self):
        return 2*self.base + 2*self.height

#Salida
circ1 = Circulo(2.5)
circ2 = Circulo(1.7)
rect1 = Rectangle(4,8)
print("Al Area del circulo 2 es", circ2.area())
print("Al Area del Rectangulo 1 es", rect1.area())
print("--------------------")
print(circ1);
print(circ2);
print("--------------------")
#Toma el __str__ del Padre (Figura)
print(rect1);