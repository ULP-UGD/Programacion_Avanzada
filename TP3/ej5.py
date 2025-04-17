'''
Ejercicio 5 
Crear una función mostrar_info_usuario que imprima todos los datos que recibe. 
Utiliza *kwargs.
'''
def mostrar_info_usuario(**kwargs) -> None:
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info_usuario(nombre="Ana", email="ana@gmail.com", edad=25)
print()
mostrar_info_usuario(nombre="Leo", email="leo@example.com", edad=30, profesion="Ingeniero")