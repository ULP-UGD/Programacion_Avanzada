"""
Ejercicio 12 (usando while) 
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el 
usuario escriba “salir” que terminará. 
"""
while True:
    entrada = input("Decí algo (o escribí 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("¡Ciao ciao!")
        break
    print("Eco:", entrada)