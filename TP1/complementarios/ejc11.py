"""
Ejercicio 11
Idem al ejercicio 10, pero simulando match con un diccionario. 
"""
dias_semana = {
    1: "DOMINGO",
    2: "LUNES",
    3: "MARTES",
    4: "MIÉRCOLES",
    5: "JUEVES",
    6: "VIERNES",
    7: "SÁBADO"
}

numero = int(input("Ingrese un número del 1 al 7: "))

dia = dias_semana.get(numero)

if dia:
    print(dia)
else:
    print("Número inválido. Debe estar entre 1 y 7.")