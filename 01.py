Escriba un programa que calcule e imprima el valor de acuerdo con lo dado
fórmula:
Q = raíz cuadrada de [(2 * C * D) / H]
Los siguientes son los valores fijos de C y H:
C es 50. H es 30.
D es la variable cuyos valores se deben ingresar a su programa en un
secuencia separada por comas
Ejemplo
Supongamos que la siguiente secuencia de entrada separada por comas es
dado al programa:
100,150,180
El resultado del programa debe ser:
18,22,24
 
Sugerencias:
Si la salida recibida está en forma decimal, debe redondearse
a su valor más cercano (por ejemplo, si la salida recibida es 26.0,
debe imprimirse como 26)
En caso de que se suministren datos de entrada a la pregunta, se debe suponer
ser una entrada de consola

"""PEDRO"""

"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.
"""
def imprimir():
    numero=[]
    for i in range(20000,32000):
        if (i%7==0 and i%5!=0) :
            numero.append(i)
    print (numero)


imprimir()

<<<<<<< HEAD
"""



def lista():
    lista2 = []

    for i in range(20000,32000):
        if i % 7 == 0 and i %5 != 0:

            lista2.append(i)
    print (lista2)

lista()




=======
>>>>>>> 1575cf54374648d680f528485743f2b0c4523a66
