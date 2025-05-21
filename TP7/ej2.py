"""
Ejercicio 2 - Radiobutton 
Crear una interfaz con tres controles de tipo Radiobutton etiquetados "Rojo", "Verde" y 
"Azul". Cuando el usuario seleccione uno de los botones, el color de fondo de la ventana 
debe cambiar al color correspondiente. 
Si la variable ventana1 representa la ventana principal (instancia de tk.Tk), podés usar el 
método .configure() para cambiar el fondo, indicando el color deseado mediante el 
parámetro bg.  
Por ejemplo: ventana1.configure(bg="red")   # para rojo 
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

# --- Constantes de Colores ---
COLOR_ROJO = "red"
COLOR_VERDE = "green"
COLOR_AZUL = "blue"
COLOR_FONDO_INICIAL = "#ECECEC"

# --- Función para cambiar el color de fondo ---
def cambiar_color_fondo():
    """
    Obtiene el color seleccionado en el Radiobutton y actualiza
    el color de fondo de la ventana principal y del frame de radios.
    También actualiza el estilo de los widgets dentro del frame.
    """
    color_seleccionado = variable_color.get()
    ventana.configure(bg=color_seleccionado)
    frame_radios.configure(style="Colored.TFrame") 
    label_titulo.configure(background=color_seleccionado) 


    style.configure("Colored.TFrame", background=color_seleccionado)
    style.configure("TRadiobutton",
                    font=radio_font,
                    background=color_seleccionado,
                    padding=5)



# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Ejercicio 2 - Cambio de Color")
ventana.geometry("300x250")
ventana.configure(bg=COLOR_FONDO_INICIAL)

# --- Definición de Fuentes ---
radio_font = tkFont.Font(family="Helvetica", size=11)
titulo_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

# --- Estilos ttk  ---
style = ttk.Style()
style.theme_use('vista')

# Estilo inicial para el Frame
style.configure("TFrame", background=COLOR_FONDO_INICIAL)
# Creamos un estilo específico para el frame que cambiará de color
style.configure("Colored.TFrame", background=COLOR_FONDO_INICIAL)


style.configure("TRadiobutton",
                font=radio_font,
                background=COLOR_FONDO_INICIAL,
                padding=5)

style.configure("TLabel",
                font=titulo_font,
                background=COLOR_FONDO_INICIAL)

# --- Variable de Control para los Radiobuttons ---
variable_color = tk.StringVar()
variable_color.set(COLOR_FONDO_INICIAL) 

# Etiqueta de titulo
label_titulo = ttk.Label(ventana, text="Selecciona un color:")
label_titulo.pack(pady=10)

# Frame para agrupar los Radiobuttons
frame_radios = ttk.Frame(ventana, style="TFrame")
frame_radios.pack(pady=10, padx=10, fill='x', expand=True)


# Radiobutton para "Rojo"
radio_rojo = ttk.Radiobutton(frame_radios,
                             text="Rojo",
                             variable=variable_color,
                             value=COLOR_ROJO,
                             command=cambiar_color_fondo,
                             style="TRadiobutton") 
radio_rojo.pack(anchor="w", padx=20, pady=5)

# Radiobutton para "Verde"
radio_verde = ttk.Radiobutton(frame_radios,
                              text="Verde",
                              variable=variable_color,
                              value=COLOR_VERDE,
                              command=cambiar_color_fondo,
                              style="TRadiobutton")
radio_verde.pack(anchor="w", padx=20, pady=5)

# Radiobutton para "Azul"
radio_azul = ttk.Radiobutton(frame_radios,
                             text="Azul",
                             variable=variable_color,
                             value=COLOR_AZUL,
                             command=cambiar_color_fondo,
                             style="TRadiobutton")
radio_azul.pack(anchor="w", padx=20, pady=5)

ventana.mainloop()