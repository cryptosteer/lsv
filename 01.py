"""PEDRO"""

"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.

"""



def lista():
    lista2 = []

    for i in range(20000,32000):
        if i % 7 == 0 and i %5 != 0:

            lista2.append(i)
    print (lista2)

lista()




