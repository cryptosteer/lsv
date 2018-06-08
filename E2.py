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

def is_palindromo(frase):
    """
    Determina si una cadena de caracteres es palindromo si o no
    :param frase: Cadena de caracteres
    :return: Retorna una cadena de caracteres: Es palindromo. O Es casi-palindromo o No es palindromo
    """
    str_clean = ''.join(frase.split(' ',)).replace(',','').lower()
    str_reverse = str_clean[::-1]
    output = 'No es polindromo'
    if str_clean == str_reverse:
        output = 'Es palindromo'
    else:
        repeat = 0
        for index, value in enumerate(str_clean):
            if (value != str_reverse[index]):
                repeat += 1
        if(repeat<=2):
            output = 'Casi palindromo'

    return output

# Ejecucion del programa
frase1 = 'Yo dono rosas, oro no doy'
frase2 = 'Isaac ni ronca asi'

print("{} ---> {}".format(frase1, is_palindromo(frase1)))
print("{} ---> {}".format(frase2, is_palindromo(frase2)))
