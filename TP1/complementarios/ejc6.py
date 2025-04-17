"""
Ejercicio 6
Calcular el perímetro y área de un triángulo, ingresar los datos por consola.
 Antes de realizar los cálculos, verificar que los datos corresponden a un triángulo.
"""
import math

while True:
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))
        
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        break
    else:
        print("Error: Los lados no forman un triángulo válido.")

# Calcular el perímetro
perimetro = lado1 + lado2 + lado3

# Calcular el semiperímetro
semiperimetro = perimetro / 2

# Calcular el área usando la fórmula de Herón
area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))

# Mostrar los resultados
print(f"Perímetro del triángulo: {perimetro}")
print(f"Área del triángulo: {area:.2f}")