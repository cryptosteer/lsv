"""PEDRO"""

c = 0
l1 = [7, 5, 14, 35]
l2 = []
for i in l1:
    if i % 7 == 0 and i %5 != 0:

        l2[c] = i
        c = c+1
        print(l2)
    else: print("No existen numeros que cumplan con lo requerido")




"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.

"""