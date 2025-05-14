# Ejercicio 3
# Escribir un programa para gestionar una agenda telefónica con los nombres y los teléfonos
# de los clientes de una empresa. El programa incluir las funciones:
# ● def busca_contacto(archivo, cliente):
#     '''
#     Función que devuelve el teléfono de un cliente de un fichero dado.
#     Parámetros:
#         archivo: Es un fichero con los nombres y teléfonos de clientes.
#         cliente: Es una cadena con el nombre del cliente.
#     Devuelve: El teléfono del cliente guardado en el fichero o un mensaje de
#     error si el teléfono o el fichero no existe.
#     '''
# ● def agrega_contacto(archivo, cliente, telf):
#     '''
#     Función que añade el teléfono de un cliente de un fichero dado.
#     Parámetros:
#         file: Es un fichero con los nombres y teléfonos de clientes.
#         cliente: Es una cadena con el nombre del cliente.
#         telf: Es una cadena con el teléfono del cliente.
#     Devuelve:
#         Un mensaje informando sobre si el teléfono se ha añadido o ha habido
#         algún problema.
#     '''
# ● def elimina_contacto(archivo, cliente):
#     '''
#     Función que elimina el teléfono de un fichero dado.
#     Parámetros:
#         file: Es un fichero con los nombres y teléfonos de contacto.
#         cliente: Es una cadena con el nombre del contacto.
#     Devuelve:
#         Un mensaje informando sobre si el teléfono se ha borrado o ha habido
#         algún problema.
#     '''
# ● def crea_directorio(archivo):
#     '''
#     Función que crea un fichero vacío para guardar una agenda telefónica.
#     Parámetros:
#         archivo: Es un fichero.
#     Devuelve:
#         Un mensaje informando sobre si el fichero se ha creado correctamente o
#         no.
#     '''
# ● def menu():
#     '''
#     Función que presenta un menú con las operaciones disponibles y devuelve
#     la opción seleccionada por el usuario.
#     Devuelve:
#         La opción seleccionada por el usuario.
#     '''
# ● def Principal():
#     '''
#     Función que lanza la aplicación
#     '''
# ●
# Crear el fichero con una agenda telefónica si no existe, para consultar el teléfono de un
# cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. La agenda
# debe estar guardada en el fichero de texto agenda.txt donde el nombre del cliente y su
# teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

def crea_directorio(archivo):
    try:
        with open(archivo, 'x') as f:
            return f"Fichero {archivo} creado correctamente."
    except FileExistsError:
        return f"El fichero {archivo} ya existe."
    except Exception as e:
        return f"Error al crear el fichero {archivo}: {e}"
##################################################################################################
##################################################################################################


def busca_contacto(archivo, cliente):
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                nombre, telefono = linea.strip().split(',')
                if nombre.strip().lower() == cliente.strip().lower():
                    return telefono.strip()
            return f"No se encontró el cliente {cliente} en el fichero."
    except FileNotFoundError:
        return f"El fichero {archivo} no existe."
    except Exception as e:
        return f"Error al buscar el contacto: {e}"
##################################################################################################
##################################################################################################


def agrega_contacto(archivo, cliente, telf):
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                nombre, _ = linea.strip().split(',')
                if nombre.strip().lower() == cliente.strip().lower():
                    return f"El cliente {cliente} ya existe en el fichero."

        with open(archivo, 'a') as f:
            f.write(f"{cliente.strip()},{telf.strip()}\n")
        return f"Contacto {cliente} con teléfono {telf} añadido correctamente."
    except FileNotFoundError:
        return f"El fichero {archivo} no existe."
    except Exception as e:
        return f"Error al añadir el contacto: {e}"
##################################################################################################
##################################################################################################


def elimina_contacto(archivo, cliente):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        encontrado = False
        nuevas_lineas = []
        for linea in lineas:
            nombre, _ = linea.strip().split(',')
            if nombre.strip().lower() != cliente.strip().lower():
                nuevas_lineas.append(linea)
            else:
                encontrado = True

        if not encontrado:
            return f"No se encontró el cliente {cliente} en el fichero."

        with open(archivo, 'w') as f:
            f.writelines(nuevas_lineas)
        return f"Contacto {cliente} eliminado correctamente."
    except FileNotFoundError:
        return f"El fichero {archivo} no existe."
    except Exception as e:
        return f"Error al eliminar el contacto: {e}"
##################################################################################################
##################################################################################################


def menu():
    print("\n=== Agenda Telefónica ===")
    print("1. Crear fichero de agenda")
    print("2. Buscar contacto")
    print("3. Añadir contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Selecciona una opción (1-5): ")
    return opcion
##################################################################################################
##################################################################################################


def principal():
    archivo = "TP4/agenda.txt"  # Ruta relativa al fichero en TP4

    while True:
        opcion = menu()

        match opcion:
            case '1':
                print(crea_directorio(archivo))
            case '2':
                cliente = input("Introduce el nombre del cliente: ")
                print(busca_contacto(archivo, cliente))
            case '3':
                cliente = input("Introduce el nombre del cliente: ")
                telefono = input("Introduce el teléfono del cliente: ")
                print(agrega_contacto(archivo, cliente, telefono))
            case '4':
                cliente = input("Introduce el nombre del cliente: ")
                print(elimina_contacto(archivo, cliente))
            case '5':
                print("Hasta pronto!!!")
                break
            case _:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")


##################################################################################################
##################################################################################################
principal()
