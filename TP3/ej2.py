'''
Ejercicio 2 
Crear una función crear_usuario que reciba nombre, email, y edad (parámetro por 
defecto 18), y retorne un diccionario con esos datos. 
Luego invocar de la siguiente manera: 
print(crear_usuario("Ana", "ana@gmail.com")) 
print(crear_usuario(email="leo@example.com", nombre="Leo", edad=25))
'''
def crear_usuario(nombre, email, edad = 18):
    return {
        "nombre": nombre,
        "email": email,
        "edad": edad
    }

print(crear_usuario("Ana", "ana@gmail.com"))
print(crear_usuario(email="leo@example.com", nombre="Leo", edad=25))