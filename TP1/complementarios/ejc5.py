"""
Ejercicio 5
Calcular el perímetro y área de un triángulo, ingresar los datos por consola.
"""
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

perimetro = lado1 + lado2 + lado3

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2

print(f"Perímetro del triángulo: {perimetro}")
print(f"Área del triángulo: {area}")
