"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def serie_fibonacci(target: int):
    serie = [0, 1]
    for i in range(target):
        if len(serie) == target:
            return serie
        serie.append(serie[i] + serie[i+1])

print(serie_fibonacci(50))