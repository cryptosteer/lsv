"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number.

Most popular number appears more times that the others into given array.

If two numbers are equal of popularity algorith must return the minor of them.

Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)

"""


def popular(l):
    """Declaro un diccionario para guardar los valores de la lista con relacion a las veces que se repiten"""
    numero = dict()

    """Recorro la lista"""
    for num in l:
        """Verifico si el valor existe en el diccionario como llave"""
        if num not in numero.keys():
            """Si no existe lo guarda"""
            numero[num] = 1
        else:
            """Si existe suma el valor de dicha llave"""
            numero[num] = numero[num] + 1

    """Declaro un valor2 para hacer la comparacion con los valores que obtengo del diccionario"""
    """Declaro un popular para guardar el valor que mas se repite"""
    valor2 = 0
    popular = 0
    for valor in numero.values():
        if valor2 == 0:
            """Guardo el primer valor del diccionario en valor2 para en la proxima iteracion hacer las comparaciones"""
            valor2 = valor
        else:
            """Comparo y guardo el valor mayor"""
            if valor > valor2:
                popular = valor

    """Obtengo las llaves del diccionario"""
    llaves = numero.keys()
    for key in llaves:
        """Comparo el valor de popular con el del diccionario de una especifica llave, si es igual guarda la llave"""
        if numero[key] == popular:
            popular = key

    """Retorno el numero mas popular"""
    return popular


lista = [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
print("{} is the most popular.".format(popular(lista)))
