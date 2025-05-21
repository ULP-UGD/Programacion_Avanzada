"""
Ejercicio 4- Listbox 
Disponer un Listbox con una serie de nombres de frutas. Permitir la selección de varias 
frutas. Cuando se presione un botón recuperar todas las frutas seleccionadas y mostrarlas 
en una Label. 
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

# --- Constantes de Estilo  ---
BG_COLOR = "#f0f0f0"
LISTBOX_BG_COLOR = "#FFFFFF"
LISTBOX_SELECT_BG_COLOR = "#0078D7"
LISTBOX_SELECT_FG_COLOR = "#FFFFFF" 
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT_COLOR = "#FFFFFF"
TEXT_COLOR = "#333333"
LABEL_RESULTADO_COLOR = "#005A9E" 

# --- Función para mostrar las frutas seleccionadas ---
def mostrar_seleccion():
    """
    Recupera todas las frutas seleccionadas del Listbox
    y las muestra en la etiqueta de resultado.
    """
    seleccionados_indices = listbox_frutas.curselection() 

    if not seleccionados_indices:
        label_resultado.config(text="No has seleccionado ninguna fruta.")
        return

    frutas_seleccionadas = []
    for indice in seleccionados_indices:
        frutas_seleccionadas.append(listbox_frutas.get(indice))

    if frutas_seleccionadas:
        texto_resultado = "Frutas seleccionadas: " + ", ".join(frutas_seleccionadas)
        label_resultado.config(text=texto_resultado)
    else:
        label_resultado.config(text="No has seleccionado ninguna fruta.")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Ejercicio 4 - Selección de Frutas")
ventana.geometry("400x350") 
ventana.configure(bg=BG_COLOR)
ventana.resizable(False, False)

# --- Definición de Fuentes ---
default_font = tkFont.Font(family="Helvetica", size=10)
listbox_font = tkFont.Font(family="Helvetica", size=11)
button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
label_font = tkFont.Font(family="Helvetica", size=11)

# --- Estilos ttk---
style = ttk.Style()
style.theme_use('clam')

style.configure("TButton", font=button_font, padding=6)
style.map("TButton",
          background=[('active', BUTTON_COLOR), ('!disabled', BUTTON_COLOR)],
          foreground=[('active', BUTTON_TEXT_COLOR), ('!disabled', BUTTON_TEXT_COLOR)])

style.configure("TLabel", font=label_font, background=BG_COLOR, foreground=TEXT_COLOR)
style.configure("Resultado.TLabel", font=label_font, background=BG_COLOR, foreground=LABEL_RESULTADO_COLOR)


# Etiqueta de instrucción
label_instruccion = ttk.Label(ventana, text="Selecciona tus frutas favoritas:")
label_instruccion.pack(pady=(10,5))

# Frame para el Listbox y Scrollbar
frame_listbox = tk.Frame(ventana, bg=BG_COLOR) 
frame_listbox.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

# Scrollbar para el Listbox
scrollbar_frutas = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)

# Listbox para las frutas
listbox_frutas = tk.Listbox(frame_listbox,
                             selectmode=tk.EXTENDED, 
                             font=listbox_font,
                             bg=LISTBOX_BG_COLOR,
                             fg=TEXT_COLOR,
                             selectbackground=LISTBOX_SELECT_BG_COLOR, 
                             selectforeground=LISTBOX_SELECT_FG_COLOR, 
                             yscrollcommand=scrollbar_frutas.set, 
                             height=6) 

# Llenar el Listbox con frutas
frutas = ["Manzana", "Banana", "Naranja", "Uva", "Frutilla", "Kiwi", "Mango", "Pera", "Ananá", "Cereza"]
for fruta in frutas:
    listbox_frutas.insert(tk.END, fruta)

# Configurar la scrollbar y empaquetarla
scrollbar_frutas.config(command=listbox_frutas.yview)
scrollbar_frutas.pack(side=tk.RIGHT, fill=tk.Y)
listbox_frutas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Botón para mostrar la selección
boton_mostrar = ttk.Button(ventana,
                           text="Mostrar Selección",
                           command=mostrar_seleccion)
boton_mostrar.pack(pady=10)

# Etiqueta para mostrar el resultado de la selección
label_resultado = ttk.Label(ventana, text="", style="Resultado.TLabel", wraplength=350)
label_resultado.pack(pady=10, padx=20)

ventana.mainloop()