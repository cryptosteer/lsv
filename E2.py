"""
Dada una cadena de caracteres determine si dicha cadena:

    1. Es palindromo
    2. Es casi-palindromo
    3. No es palindromo

Casi-palindromo con aquellas cadenas que por un caracter pueden ser palindromo:

    Ej: 
        "Yo dono rosas, oro no doy" ---> Palindromo
        "Isaac ni ronca asi" ---> Casi-palindromo
"""
from functools import reduce


def remove_space_and_lower(frase):
    return frase.lower().replace(' ', '')


def is_palindromo(frase):
    frase_original = remove_space_and_lower(frase)
    frase_invertida = remove_space_and_lower(frase[::-1])
    data_comparations = list(map(lambda x, y: x == y, frase_invertida, frase_original))
    return reduce(lambda x: x==False, data_comparations, initial=0)


print(is_palindromo('Isaac ni ronca asi'))
