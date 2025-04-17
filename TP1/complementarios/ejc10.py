"""
Estructura selectiva múltiple
Ejercicio 10
Ingresar por teclado un número entre 1 y 7, mostrar 
a qué día de la semana corresponde el número ingresado. 
Por ejemplo, si ingresa 1, muestra DOMINGO. Usar match. 
"""
numero = int(input("Ingrese un número del 1 al 7: "))

match numero:
    case 1:
        print("DOMINGO")
    case 2:
        print("LUNES")
    case 3:
        print("MARTES")
    case 4:
        print("MIÉRCOLES")
    case 5:
        print("JUEVES")
    case 6:
        print("VIERNES")
    case 7:
        print("SÁBADO")
    case _:
        print("Número inválido. Debe estar entre 1 y 7.")