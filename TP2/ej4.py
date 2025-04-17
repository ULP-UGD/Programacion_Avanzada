'''
Ejercicio 4 
Dado un diccionario que representa un cliente con posibles claves "nombre", "edad" y 
"profesion". para identificar si: 
● Es mayor de edad (edad >= 18) 
● Es menor 
● No se indica la edad 
crear la función clasificar_cliente(cliente) 
# Ejemplo: {"nombre": "Ana", "edad": 17} → "Menor de edad" 
# {"nombre": "Carlos", "edad": 21, "profesion": "médico"} → "Mayor de edad" 
# {"nombre": "Lucía"} → "Edad no especificada"
'''

def clasificar_cliente(cliente):
    if "edad" in cliente:
        if cliente["edad"] >= 18:
            return "Mayor de edad"
        else:
            return "Menor de edad"
    else:
        return "Edad no especificada"

print(clasificar_cliente({"nombre": "Ana", "edad": 17}))

print(clasificar_cliente({"nombre": "Carlos", "edad": 21, "profesion": "médico"}))

print(clasificar_cliente({"nombre": "Lucía"}))