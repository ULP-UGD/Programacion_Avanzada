"""
Ejercicio 2
 Se necesita obtener el promedio simple de un estudiante a partir de sus tres notas parciales N1, N2 y N3.
"""
n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))

promedio = (n1 + n2 + n3) / 3

print(f"El promedio del estudiante es: {promedio:.2f}")