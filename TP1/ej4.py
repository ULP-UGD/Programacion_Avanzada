"""
Ejercicio 4 
Pedir una cadena y dos índices (inicio y fin),
 y mostrar la subcadena que se encuentra entre esos índices. 
"""
cadena = input("Ingrese una cadena: ")

inicio = int(input("Índice de inicio: "))

fin = int(input("Índice de fin: "))


subcadena = cadena[inicio:fin]

print("Subcadena:", subcadena)