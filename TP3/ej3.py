'''
Ejercicio 3 
Crear una función sumar_todo que acepte cualquier cantidad de números y retorne la 
suma.
'''
def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1, 2, 3))
print(sumar_todo(10, 20, 30, 40))
print(sumar_todo())