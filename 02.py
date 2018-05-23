"""
Write a program that calculates and prints the value according to the given
formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is
given to the program:
100,150,180
The output of the program should be:
18,22,24


Hints:
If the output received is in decimal form, it should be rounded
off to its nearest value (for example, if the output received is 26.0,
it should be printed as 26)
In case of input data being supplied to the question, it should be assumed
to be a console input.
"""
c, h=50,30
def Calcular(lista):
    resultado=[]
    for x in lista:
        resultado.append(((2*c*x)/h)**(1/2))
    return resultado

"""def Convertir(lista):
    listaconvertida=[]
    r=""
    for x in lista:
        if x==",":
            if r!="":
                listaconvertida.append(int(r))
            r=""
        else:
            r=r+x
    listaconvertida.append(int(r))
    return listaconvertida"""
#lista=Convertir("100,150,180")
#lista = [int(numero) for numero in ("100,150,180").split(',')]
lista = [int(numero) for numero in (input("Ingrese los numeros a evaluar: ")).split(',')]
#Para no mostrar los corchetes del arreglo
print(str(lista)[1:-1])
resultado=Calcular(lista)
mostrar=""
#Cambiar tipo de dato para que se presenten como enteros
for x in resultado:
    mostrar=mostrar+str(int(x))+", "
print(mostrar[:-2])