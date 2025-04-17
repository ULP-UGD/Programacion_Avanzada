"""
Ejercicio 8 (usando for) 
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas. 
"""
n = int(input("Ingrese un número entero positivo: "))

cuenta_regresiva = [str(i) for i in range(n, -1, -1)]

print(", ".join(cuenta_regresiva))