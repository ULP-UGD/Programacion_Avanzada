"""
Ejercicio 7
Calcular el perímetro y área de un círculo. Tener en cuenta que PI es una constante.
"""
import math

radio = float(input("Ingrese el radio del círculo: "))

perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)

print(f"Perímetro del círculo: {perimetro:.2f}")
print(f"Área del círculo: {area:.2f}")