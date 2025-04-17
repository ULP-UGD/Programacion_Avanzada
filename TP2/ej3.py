'''
Ejercicio 3 
Implementar una función que reciba una cadena que indique el día de la semana y devuelva 
si es “Laboral”, “Fin de semana” o “No válido”. Usar match. 
'''
def clasificar_dia(dia):
    dia = dia.lower()
    
    match dia:
        case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
            return "Laboral"
        case "sábado" | "domingo":
            return "Fin de semana"
        case _:
            return "No válido"


print(clasificar_dia("lunes"))
print(clasificar_dia("sábado"))
print(clasificar_dia("osvaldo"))