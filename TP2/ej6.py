'''
Ejercicio 6 
Dadas dos listas del mismo tamaño, usá zip para obtener una lista con la suma de los 
elementos correspondientes. 
lista1 = [1, 2, 3] 
lista2 = [4, 5, 6] 
# Resultado esperado: [5, 7, 9]
'''

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = [a + b for a, b in zip(lista1, lista2)]

print(resultado)