"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
class Circulo:
    PI = 3.1416
    def __init__(self, radio=0.0):
        self.radio = radio

    def area(self):
        return self.PI*(self.radio**2)

    def perimeter(self):
        return 2*self.PI*self.radio

    def __str__(self):
        rep = "Circulo de radio: ".format(self.radio)+"\n"
        rep += "Area: {0} y perimetro {1}".format(self.area(), self.perimeter())
        return rep

#Salida
circ1 = Circulo(2.5)
circ2 = Circulo(1.7)
circ3 = Circulo()
print("Al Area del circulo 2 es", circ2.area())
print("--------------------")
print(circ1);
print(circ2);
print(circ3);