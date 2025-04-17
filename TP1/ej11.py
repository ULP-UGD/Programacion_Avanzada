"""
Ejercicio 11 (usando for) 
Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10. 
"""
for i in range(1, 11):
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        print(f"{i} × {j} = {i * j}")