'''
Ejercicio 2 
Generar una matriz de 3x3 con los números del 1 al 9 usando comprensión de listas 
anidadas. 
# Resultado esperado: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
'''
n = 3
matriz = [[i * n + j + 1 for j in range(n)] for i in range(n)]

print("Matriz 3x3:")
print(matriz)
