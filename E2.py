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
    # Complete
    """Convertimos la cadena en minuscula y remplazamos los valoresde espacios y resplazamos sin espacio"""
    minuscula = frase
    cadena=minuscula.lower().replace(' ', '').replace(',', '')
    x = cadena == cadena[::-1]
    if x is True:
        return "polindromo"
    else:
        return "no es polindromo"

print("{} ---> {}".format(frase, is_palindromo(frase)))
