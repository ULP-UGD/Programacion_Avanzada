'''
Ejercicio 1 
Escribir una función que pida un número entero entre 1 y 10,
 lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
donde “n” es el número introducido, y la muestre por pantalla. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello. 
'''
def mostrar_tabla_multiplicar():
    try:
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        
        if numero < 1 or numero > 10:
            print("El número debe estar entre 1 y 10")
            return
        
        nombre_fichero = f"TP4/tabla-{numero}.txt"
        with open(nombre_fichero, 'r') as fichero:
            print(f"\nTabla de multiplicar del {numero}:")
            print(fichero.read())
            
    except ValueError:
        print("Por favor, introduce un número entero válido")
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no existe")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

mostrar_tabla_multiplicar()