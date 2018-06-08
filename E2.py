"""
Dada una cadena de caracteres determine si dicha cadena:

    1. Es palindromo
    2. Es casi-palindromo
    3. No es palindromo

Casi-palindromo con aquellas cadenas que por un caracter pueden ser palindromo:

    Ej: 
        "Yo dono rosas, oro no doy" ---> Palindromo
        yodonorosas,oronodoy

        "Isaac ni ronca así" ---> Casi-palindromo
"""
import string
import unicodedata


def is_palindromo(s):
    letras = set(string.ascii_lowercase)
    s = s.lower()
    s = ''.join([letra for letra in s if letra in letras])
    if s == s[::-1]:
        return "Palindromo"
    else:
        c = 0
        for x in range(0, len(s)):
            if s[-x-1] != s[x]:
                c = c+1
        if c <=2:
            return "Casi-palindromo"
        else:
            return "No es palindromo"
#No se aceptan frases con acentuación
frase = "Yo dono rosas, oro no doy"
print("{} ---> {}".format(frase, is_palindromo(frase)))
frase = "Isaac ni ronca asi"
print("{} ---> {}".format(frase, is_palindromo(frase)))
