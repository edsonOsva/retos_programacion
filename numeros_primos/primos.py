"""
    /*
    * Escribe un programa que se encargue de comprobar si un número es o no primo.
    * Hecho esto, imprime los números primos entre 1 y 100.
    */
"""

def isprimo(num: int):

    if num < 2: 
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
    


if __name__ == "__main__":

    lista_primos = []

    for i in range(100):
        if isprimo(i):
            lista_primos.append(i)

    print(lista_primos)