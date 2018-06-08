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
    cont = cantidad_apariciones(data_comparations)
    return final_messages(cont, frase)


def final_messages(cont, frase):
    return {
        0: '{} es palindrome'.format(frase),
        1: '{} es casi palindrome'.format(frase),
        2: '{} no es palindrome'.format(frase)
    }.get(cont, None)


def cantidad_apariciones(data_comparations):
    cont = 0
    for item in data_comparations:
        if not item:
            cont += 1
    return cont


print(is_palindromo('Isaac ni ronca asi'))
