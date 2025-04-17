'''
Ejercicio 6 
Crear una función operar_lista(lista, operacion) que reciba una lista de números 
y una función que defina qué operación aplicar sobre la lista (suma o multipliacr sus 
elementos). La idea es practicar pasar funciones por parámetro.
'''

def sumar(lista):
    return sum(lista)

def multiplicar(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def operar_lista(lista, operacion):
    return operacion(lista)

numeros = [1, 2, 3, 4]

print(operar_lista(numeros, sumar))

print(operar_lista(numeros, multiplicar))