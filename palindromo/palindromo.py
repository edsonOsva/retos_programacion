"""
    Implemente, tanto de forma recursiva como de forma iterativa, una función que nos
    diga si una cadena de caracteres es simétrica (un palíndromo). Por ejemplo,
    “DABALEARROZALAZORRAELABAD” es un palíndromo.
"""

def isPalindromo(cadena: str):
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace(",", "")
    cadena = cadena.lower()
    original = cadena[::]
    volteada = original[::-1]
    if original == volteada:
        return True
    else:
        return False


print(isPalindromo("A Mercedes, ese de crema"))