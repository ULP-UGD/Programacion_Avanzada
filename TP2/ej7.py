'''
Ejercicio 7 
Dadas dos listas, una con nombres y otra con apellidos, usá zip para generar una lista con 
los nombres completos. 
nombres = ["Ana", "Luis", "Carla"] 
apellidos = ["Pérez", "Gómez", "Ruiz"] 
# Resultado esperado: ["Ana Pérez", "Luis Gómez", "Carla Ruiz"]
'''
nombres = ["Ana", "Luis", "Carla"]
apellidos = ["Pérez", "Gómez", "Ruiz"]

nombres_completos = [nombre + " " + apellido for nombre, apellido in zip(nombres, apellidos)]

print(nombres_completos)