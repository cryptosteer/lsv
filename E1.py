"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number. 

Most popular number appears more times that the others into given array.

If two numbers are equal of popularity algorith must return the minor of them.

Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)

"""
"""Se utiliza esta libreria que ayuda con las listas"""
from collections import Counter


def popular(l):
    """Determinamos cuantas veces esta repetido un numero"""
    contar=Counter(l)
    """Utilizamos el metodo most_common que Devuelve una lista de los n elementos más comunes y sus recuentos,
     del más comun."""
    popular=contar.most_common(1)[0][0]
    ##return Counter(l).most_common(1)[0][0]
    return popular

lista = [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
##print("{} is the most popular.".format(popular(lista)))
print(popular(lista))




















