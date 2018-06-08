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



def is_palindromo(frase):

    var = frase.lower().replace(' ', '').replace(',', '')
    x = var == var[::-1]
    if x is True:
        return "Es Polindromo"
    else:
        return "No es Polindromo"


frase = input("Ingrese texto numero a validar: ")
print("{} ---> {}".format(frase, is_palindromo(frase)))


