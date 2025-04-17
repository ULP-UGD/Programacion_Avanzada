"""
Ejercicio 6 
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación. 
● Ingredientes vegetarianos: Pimiento y tofu. 
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en 
todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no 
y todos los ingredientes que lleva. 
"""

pizza_tipo = input("¿Desea una pizza vegetariana (s/n)? ")

# Si el usuario quiere una pizza vegetariana
if pizza_tipo.lower() == "s":
    # Muestra el menu de ingredientes vegetarianos
    print("Ingredientes vegetarianos:")
    print("1. Pimiento")
    print("2. Tofu")
    
    # Pide al usuario que elija un ingrediente
    ingrediente_elegido = input("Ingrese el número del ingrediente que desea: ")
    
    # Verifica que el usuario haya elegido un ingrediente valido
    while ingrediente_elegido not in ["1", "2"]:
        print("Error: Ingrediente no válido. Por favor, ingrese un número del 1 al 2.")
        ingrediente_elegido = input("Ingrese el número del ingrediente que desea: ")
    
    # Convierte el numero del ingrediente a una variable que contenga el nombre del mismo
    if ingrediente_elegido == "1":
        ingrediente = "Pimiento"
    else:
        ingrediente = "Tofu"
    
    # Muestra la pizza elegida y sus ingredientes
    print("Ha elegido una pizza vegetariana con:", ingrediente)
    print("Ingredientes: Pimiento/Tofu, Mozzarella, Tomate")
    
# Si el usuario no quiere una pizza vegetariana
else:
    # Menu de ingredientes no vegetarianos
    print("Ingredientes no vegetarianos:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    
    # Pide al usuario que elija un ingrediente
    ingrediente_elegido = input("Ingrese el número del ingrediente que desea: ")
    
    # Verifica que elija una opcion valida
    while ingrediente_elegido not in ["1", "2", "3"]:
        print("Error: Ingrediente no válido. Por favor, ingrese un número del 1 al 3.")
        ingrediente_elegido = input("Ingrese el número del ingrediente que desea: ")
    
    # Convierte el numero del ingrediente a una variable que contenga el nombre del mismo
    if ingrediente_elegido == "1":
        ingrediente = "Peperoni"
    elif ingrediente_elegido == "2":
        ingrediente = "Jamón"
    else:
        ingrediente = "Salmón"
    
    # Muestra la pizza elegida y sus ingredientes
    print("Ha elegido una pizza no vegetariana con:", ingrediente)
    print("Ingredientes: Peperoni/Jamón/Salmón, Mozzarella, Tomate")
