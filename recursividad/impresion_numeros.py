"""
Crear una funcion recursiva que imprima los numeros del 100 al 0
"""

def number2zero(target: int):
    if target >= 0:
        print(target)
        number2zero(target - 1)

number2zero(100)