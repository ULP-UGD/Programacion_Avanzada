"""
Ejercicio 1 - Entry, Radiobutton, button 
Disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles 
Radiobutton permitir seleccionar si queremos sumarlos o restarlos. Al presionar un botón 
mostrar el resultado de la operación seleccionada.
"""
# Importaciones necesarias de la biblioteca Tkinter
import tkinter as tk  
from tkinter import ttk  
from tkinter import messagebox  
from tkinter import font as tkFont 

# Definición de colores para la interfaz (mejora la legibilidad y facilidad de cambio)
BG_COLOR = "#f0f0f0" 
BUTTON_COLOR = "#4CAF50" 
BUTTON_TEXT_COLOR = "#FFFFFF"  
TEXT_COLOR = "#333333" 

# --funciones--
def operar():
    """
    Realiza la operación (suma o resta) según la selección del Radiobutton
    y muestra el resultado en la etiqueta correspondiente.
    También maneja errores de entrada.
    """
    try:
        # Obtener los valores de los campos de entrada (Entry) como cadenas
        valor1_str = entry_valor1.get()
        valor2_str = entry_valor2.get()

        # Verificar si alguno de los campos está vacío
        if not valor1_str or not valor2_str:
            messagebox.showerror("Error", "Ambos valores deben contener números.")
            return  # Termina la función si hay error

        # Intentar convertir los valores a números enteros
        num1 = int(valor1_str)
        num2 = int(valor2_str)

        # Obtener la operación seleccionada del Radiobutton (a través de la variable de control)
        operacion_seleccionada = opcion_operacion.get()
        resultado = 0  # Inicializar la variable resultado

        # Realizar la operación según la selección
        if operacion_seleccionada == "sumar":
            resultado = num1 + num2
        elif operacion_seleccionada == "restar":
            resultado = num1 - num2
        else:
            # Este caso no debería ocurrir si los Radiobuttons están bien configurados
            messagebox.showerror("Error", "Seleccione una operación")
            return

        # Actualizar la etiqueta que muestra el resultado (convirtiendo el resultado a cadena)
        label_resultado_valor.config(text=str(resultado))

    except ValueError:
        # Si ocurre un error al convertir a entero (ej: el usuario ingresó texto)
        messagebox.showerror("Error de Entrada", "Ambos valores deben ser números enteros.")
        label_resultado_valor.config(text="")  
    except Exception as e:
        # Capturar cualquier otro error inesperado
        messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")
        label_resultado_valor.config(text="")  

# --ventana principal--
ventana = tk.Tk() 
ventana.title("Ejercicio 1 - Calculadora Simple") 
ventana.geometry("350x300")  
ventana.configure(bg=BG_COLOR)  
ventana.resizable(False, False)  

# --fuentes--
default_font = tkFont.Font(family="Helvetica", size=10)
label_font = tkFont.Font(family="Helvetica", size=11)
entry_font = tkFont.Font(family="Helvetica", size=10)
button_font = tkFont.Font(family="Helvetica", size=10, weight="bold") 
resultado_font = tkFont.Font(family="Helvetica", size=16, weight="bold") 

# --estilos ttk--
style = ttk.Style() 
style.theme_use("clam") 

# --estilo frames--
style.configure("TFrame", background=BG_COLOR)

# --estilo labels--
style.configure("TLabel", background=BG_COLOR, font=label_font, foreground=TEXT_COLOR)

# --estilo radiobuttons--
style.configure("TRadiobutton", background=BG_COLOR, font=default_font, foreground=TEXT_COLOR)
style.map("TRadiobutton",
          indicatorcolor=[('selected', BUTTON_COLOR), ('!selected', TEXT_COLOR)])


# --estilo button--
style.configure("TButton", font=button_font, padding=6) 
style.map("TButton",
          background=[('active', BUTTON_COLOR), ('!disabled', BUTTON_COLOR)], 
          foreground=[('active', BUTTON_TEXT_COLOR), ('!disabled', BUTTON_TEXT_COLOR)]) 

# --variables de control--
opcion_operacion = tk.StringVar()
opcion_operacion.set("restar")  


# --frame para las entradas--
frame_entradas = ttk.Frame(ventana, padding="15 15 15 10") 
frame_entradas.pack(pady=10, padx=10, fill="x")

label_valor1 = ttk.Label(frame_entradas, text="Ingrese el primer valor:")
label_valor1.grid(row=0, column=0, sticky="w", padx=5, pady=8) 
entry_valor1 = ttk.Entry(frame_entradas, width=18, font=entry_font)
entry_valor1.grid(row=0, column=1, padx=5, pady=8)

label_valor2 = ttk.Label(frame_entradas, text="Ingrese el segundo valor:")
label_valor2.grid(row=1, column=0, sticky="w", padx=5, pady=8)
entry_valor2 = ttk.Entry(frame_entradas, width=18, font=entry_font)
entry_valor2.grid(row=1, column=1, padx=5, pady=8)

# --frame para los radiobuttons--
frame_operaciones = ttk.Frame(ventana, padding="10")
frame_operaciones.pack(pady=10) 

# Radiobutton para la opción "Sumar"
radio_sumar = ttk.Radiobutton(frame_operaciones, text="Sumar", variable=opcion_operacion, value="sumar")
radio_sumar.pack(side="left", padx=15) 

# Radiobutton para la opción "Restar"
radio_restar = ttk.Radiobutton(frame_operaciones, text="Restar", variable=opcion_operacion, value="restar")
radio_restar.pack(side="left", padx=15)

# Boton para operar
boton_operar = ttk.Button(ventana, text="Operar", command=operar, style="TButton")
boton_operar.pack(pady=15, ipady=4) 

# label para mostrar el resultado
label_resultado_valor = ttk.Label(ventana, text="", font=resultado_font, foreground=BUTTON_COLOR)
label_resultado_valor.pack(pady=10) 

ventana.mainloop() 