"""
definir una funcion que calcule el factorial de un numero recibido mayor o igual que cero 
"""

def calcular_factorial(target: int):
    if target < 0:
        return "El numero debe ser un numero mayor o igual a cero"
    if target == 0:
        return 1
    return target * calcular_factorial(target - 1)

print(calcular_factorial(5))