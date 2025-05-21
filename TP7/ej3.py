"""
Ejercicio 3 - Checkbutton - Button 
Diseñar una interfaz que incluya un Checkbutton con el siguiente mensaje: 
"¿Está de acuerdo con los términos y condiciones?" 
También debe incluirse un botón que, inicialmente, esté deshabilitado. 
Cuando el usuario marque (tilde) el Checkbutton, el botón debe activarse automáticamente. 
Si se desmarca, el botón debe volver a desactivarse.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

# --- Constantes de Estilo ---
BG_COLOR = "#f0f0f0"
BUTTON_COLOR_ENABLED = "#4CAF50" 
BUTTON_COLOR_DISABLED = "#B0B0B0" 
BUTTON_TEXT_COLOR = "#FFFFFF"
TEXT_COLOR = "#333333"

# --- Función para actualizar el estado del botón ---
def actualizar_estado_boton():
    """
    Verifica el estado del Checkbutton y habilita o deshabilita
    el botón 'Continuar' en consecuencia.
    """
    if variable_acepta_terminos.get(): 
        boton_continuar.config(state=tk.NORMAL)
        style.configure("Enabled.TButton", background=BUTTON_COLOR_ENABLED)
        boton_continuar.configure(style="Enabled.TButton")
    else: 
        boton_continuar.config(state=tk.DISABLED)
        style.configure("Disabled.TButton", background=BUTTON_COLOR_DISABLED)
        boton_continuar.configure(style="Disabled.TButton")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Ejercicio 3 - Checkbutton y Botón")
ventana.geometry("400x150")
ventana.configure(bg=BG_COLOR)
ventana.resizable(False, False)

# --- Definición de Fuentes ---
default_font = tkFont.Font(family="Helvetica", size=10)
button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

# --- Estilos ttk ---
style = ttk.Style()
style.theme_use('clam') 

style.configure("TCheckbutton",
                font=default_font,
                background=BG_COLOR,
                foreground=TEXT_COLOR,
                padding=5)
style.map("TCheckbutton",
          indicatorcolor=[('selected', BUTTON_COLOR_ENABLED), ('!selected', TEXT_COLOR)])


style.configure("TButton", font=button_font, padding=6)
# Estilo para botón habilitado
style.configure("Enabled.TButton",
                font=button_font,
                padding=6,
                background=BUTTON_COLOR_ENABLED,
                foreground=BUTTON_TEXT_COLOR)
# Estilo para botón deshabilitado
style.configure("Disabled.TButton",
                font=button_font,
                padding=6,
                background=BUTTON_COLOR_DISABLED,
                foreground="#A0A0A0") 


# --- Variable de Control para el Checkbutton ---
variable_acepta_terminos = tk.BooleanVar()
variable_acepta_terminos.set(False) 


# Checkbutton para los términos y condiciones
check_terminos = ttk.Checkbutton(ventana,
                                 text="¿Está de acuerdo con los términos y condiciones?",
                                 variable=variable_acepta_terminos,
                                 command=actualizar_estado_boton, 
                                 style="TCheckbutton")
check_terminos.pack(pady=20, padx=20)

# Botón "Continuar"
boton_continuar = ttk.Button(ventana,
                             text="Continuar",
                             command=lambda: print("Botón Continuar presionado"), 
                             style="Disabled.TButton",
                             state=tk.DISABLED) 
boton_continuar.pack(pady=10)

actualizar_estado_boton()

ventana.mainloop()