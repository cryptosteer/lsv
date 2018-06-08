"""
Dada una cadena de caracteres determine si dicha cadena:

    1. Es palindromo
    2. Es casi-palindromo
    3. No es palindromo

Casi-palindromo con aquellas cadenas que por un caracter pueden ser palindromo:

    Ej: 
        "Yo dono rosas, oro no doy" ---> Palindromo
        "Isaac ni ronca así" ---> Casi-palindromo
"""
import re
from collections import Counter


def is_palindromo(frase):

    # we remove punctuation to the phrase
    frase_without_spaces =  re.sub("[ ,.;:?!]", "", frase)

    # phrase normal and upside down
    right = frase_without_spaces.lower()
    left = frase_without_spaces.lower()[::-1]

    # evaluate if al the caracter are the same
    almost = map(lambda x ,y: x ==y, right,left)

    # if all the comparison return True
    if all(almost):
        return "Es palindromo"
    else:
        # if just exist one caracter diferent
        value = dict(Counter(list(almost))).get(False) == 1

        if value:
            return "Casi palindroma"
        else:
            return "No es palindroma"


frase = "Yo dono rosas, oro no doy"
print("{} ---> {}".format(frase, is_palindromo(frase)))
