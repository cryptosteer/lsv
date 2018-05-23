"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.
"""




lista=[]
for i in range(20000, 32000):
    a=i%7
    b=i%5
    if (a==0 and b!=0):

        lista.append(i)

print(lista)
