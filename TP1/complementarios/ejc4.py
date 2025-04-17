"""
Ejercicio 4
Calcular el perímetro y área de un rectángulo, ingresar los datos por consola.
"""

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

perimetro = 2 * (base + altura)
area = base * altura


print(f"Perímetro del rectángulo: {perimetro}")
print(f"Área del rectángulo: {area}")