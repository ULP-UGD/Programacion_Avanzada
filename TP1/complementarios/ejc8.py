"""
CONDICIONALES
Ejercicio 8
Evaluar si dos N° solicitados por consola, son iguales,
 o en caso contrario identificar si el primero es mayor o menor que el segundo.
"""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 == num2:
    print("Ambos números son iguales.")
elif num1 > num2:
    print("El primer número es mayor que el segundo.")
else:
    print("El primer número es menor que el segundo.")