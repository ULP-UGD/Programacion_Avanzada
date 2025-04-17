"""
Ejercicio 7 (usando for) 
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas. 
"""
n = int(input("Ingrese un número entero positivo: "))

impares = [str(i) for i in range(1, n+1) if i % 2 != 0]

print(", ".join(impares))