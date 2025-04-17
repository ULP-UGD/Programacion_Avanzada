'''
Ejercicio 2 
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con 
la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el 
fichero no existe debe mostrar un mensaje por pantalla informando de ello. 
'''
def mostrar_linea_tabla():
    try:
        n = int(input("Introduce un número n entre 1 y 10: "))
        m = int(input("Introduce un número m entre 1 y 10: "))
        
        if n < 1 or n > 10 or m < 1 or m > 10:
            print("Ambos números deben estar entre 1 y 10")
            return
        
        nombre_fichero = f"TP4/tabla-{n}.txt"
        
        with open(nombre_fichero, 'r') as fichero:
            lineas = fichero.readlines()
            if m <= len(lineas):
                print(f"\nLínea {m} de la tabla de multiplicar del {n}:")
                print(lineas[m-1].strip())
            else:
                print(f"El fichero {nombre_fichero} no tiene {m} líneas")
                
    except ValueError:
        print("Por favor, introduce números enteros válidos")
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no existe")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

mostrar_linea_tabla()