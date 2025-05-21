"""
Ejercicio 5 -  LabelFrame, Entry, Combobox, Treeview, Button 
Diseñar una aplicación con interfaz gráfica que permita gestionar un pequeño inventario de 
productos. La interfaz debe estar organizada mediante un ttk.Notebook con dos pestañas, 
utilizando componentes como LabelFrame, Entry, Combobox, Treeview, Button, etc. 
Pestaña 1: “Registro de Producto” 
Esta pestaña debe contener un ttk.LabelFrame titulado “Datos del Producto”. Allí el usuario 
podrá ingresar: 
● Nombre del producto (Entry) 
● Precio (Entry) 
● Categoría (Combobox) con opciones como “Alimentos”, “Limpieza”, “Tecnología”, 
etc. 
También debe incluir botones: 
● Agregar producto: guarda los datos ingresados. 
● Limpiar: borra el contenido del formulario. 
Validar que el campo "Precio" sea un número válido. 
Pestaña 2: “Inventario” 
Debe incluir un ttk.Treeview con tres columnas: 
● Nombre 
● Precio 
● Categoría 
Agregá también una barra de desplazamiento vertical si hay muchos productos. 
Debajo del Treeview, incluir botones: 
● Eliminar producto seleccionado 
● Ver detalles: abre una ventana secundaria (Toplevel) mostrando los datos completos 
del producto en un Label o Messagebox 
"""
import customtkinter as ctk
from tkinter import ttk, messagebox

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

# --- Variables Globales ---
inventario_productos = []
id_actual_producto = 0

# --- Funciones ---
def validar_precio(precio_str):
    """Valida si el precio ingresado es un número flotante positivo."""
    try:
        precio = float(precio_str)
        return precio > 0
    except ValueError:
        return False

def agregar_producto():
    """Agrega un producto al inventario y al Treeview."""
    global id_actual_producto
    nombre = entry_nombre.get()
    precio_str = entry_precio.get()
    categoria = combo_categoria.get()

    if not nombre or not precio_str or not categoria:
        messagebox.showwarning("Campos Vacíos", "Todos los campos son obligatorios.")
        return

    if not validar_precio(precio_str):
        messagebox.showerror("Error de Precio", "El precio debe ser un número positivo válido.")
        entry_precio.focus()
        return

    precio = float(precio_str)
    id_actual_producto += 1
    
    nuevo_producto = {
        "id": id_actual_producto,
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria
    }
    inventario_productos.append(nuevo_producto)
    
    # Insertar en el Treeview con colores alternos
    tags = ('evenrow',) if id_actual_producto % 2 == 0 else ('oddrow',)
    tree_inventario.insert("", "end", iid=str(id_actual_producto), 
                          values=(nombre, f"${precio:.2f}", categoria),
                          tags=tags)
    
    messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
    limpiar_formulario()

def limpiar_formulario():
    """Limpia los campos del formulario."""
    entry_nombre.delete(0, "end")
    entry_precio.delete(0, "end")
    combo_categoria.set("")
    entry_nombre.focus()

def eliminar_producto_seleccionado():
    """Elimina el producto seleccionado."""
    seleccion = tree_inventario.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")
        return
    
    if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este producto?"):
        item_id = int(seleccion[0])
        tree_inventario.delete(seleccion[0])
        global inventario_productos
        inventario_productos = [p for p in inventario_productos if p["id"] != item_id]
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")

def ver_detalles_producto():
    """Muestra los detalles del producto seleccionado."""
    seleccion = tree_inventario.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un producto para ver detalles.")
        return
    
    item_id = int(seleccion[0])
    producto = next((p for p in inventario_productos if p["id"] == item_id), None)
    
    if producto:
        detalles = f"ID: {producto['id']}\n\n"
        detalles += f"Nombre: {producto['nombre']}\n\n"
        detalles += f"Precio: ${producto['precio']:.2f}\n\n"
        detalles += f"Categoría: {producto['categoria']}"
        
        # Crear ventana de detalles
        detalle_window = ctk.CTkToplevel(app)
        detalle_window.title("Detalles del Producto")
        detalle_window.geometry("400x300")
        detalle_window.transient(app)
        detalle_window.grab_set()
        
        frame = ctk.CTkFrame(detalle_window)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        label = ctk.CTkLabel(frame, text=detalles, font=("Arial", 14), 
                            justify="left")
        label.pack(pady=20, padx=20)
        
        btn_cerrar = ctk.CTkButton(frame, text="Cerrar", 
                                  command=detalle_window.destroy)
        btn_cerrar.pack(pady=10)
    else:
        messagebox.showerror("Error", "No se encontró el producto seleccionado.")

# --- Interfaz Principal ---
app = ctk.CTk()
app.title("Gestión de Inventario - CustomTkinter")
app.geometry("800x600")

# Crear pestañas
tabview = ctk.CTkTabview(app)
tabview.pack(pady=10, padx=10, fill="both", expand=True)

# Pestaña 1: Registro de Producto
tab_registro = tabview.add("Registro")
tab_inventario = tabview.add("Inventario")

# --- Pestaña Registro ---
frame_registro = ctk.CTkFrame(tab_registro)
frame_registro.pack(pady=20, padx=20, fill="both", expand=True)

label_titulo = ctk.CTkLabel(frame_registro, text="Datos del Producto", 
                           font=("Arial", 16, "bold"))
label_titulo.pack(pady=(0, 20))

# Formulario
form_frame = ctk.CTkFrame(frame_registro)
form_frame.pack(fill="x", padx=50, pady=10)

# Nombre
ctk.CTkLabel(form_frame, text="Nombre del Producto:").grid(row=0, column=0, 
                                                          padx=10, pady=10, sticky="e")
entry_nombre = ctk.CTkEntry(form_frame, width=300)
entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Precio
ctk.CTkLabel(form_frame, text="Precio:").grid(row=1, column=0, 
                                             padx=10, pady=10, sticky="e")
entry_precio = ctk.CTkEntry(form_frame, width=300)
entry_precio.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Categoría
ctk.CTkLabel(form_frame, text="Categoría:").grid(row=2, column=0, 
                                                padx=10, pady=10, sticky="e")
categorias = ["Alimentos", "Limpieza", "Tecnología", "Hogar", "Ropa", "Electrónicos"]
combo_categoria = ctk.CTkComboBox(form_frame, values=categorias, width=300)
combo_categoria.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Botones
btn_frame = ctk.CTkFrame(frame_registro)
btn_frame.pack(pady=20)

btn_agregar = ctk.CTkButton(btn_frame, text="Agregar Producto", 
                           command=agregar_producto, width=150)
btn_agregar.pack(side="left", padx=10)

btn_limpiar = ctk.CTkButton(btn_frame, text="Limpiar Formulario", 
                           command=limpiar_formulario, width=150)
btn_limpiar.pack(side="left", padx=10)

# --- Pestaña Inventario ---
frame_inventario = ctk.CTkFrame(tab_inventario)
frame_inventario.pack(pady=20, padx=20, fill="both", expand=True)

# Treeview 
tree_frame = ctk.CTkFrame(frame_inventario)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", 
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#2a2d2e",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])
style.configure("Treeview.Heading", 
                background="#3b8ed0", 
                foreground="white",
                relief="flat")
style.map("Treeview.Heading", 
          background=[('active', '#1f6aa5')])

tree_inventario = ttk.Treeview(tree_frame, columns=("Nombre", "Precio", "Categoría"), 
                              show="headings", height=15)

tree_inventario.heading("Nombre", text="Nombre")
tree_inventario.heading("Precio", text="Precio")
tree_inventario.heading("Categoría", text="Categoría")

tree_inventario.column("Nombre", width=300, anchor="w")
tree_inventario.column("Precio", width=150, anchor="center")
tree_inventario.column("Categoría", width=200, anchor="w")

# Scrollbars
scroll_y = ctk.CTkScrollbar(tree_frame, orientation="vertical", command=tree_inventario.yview)
scroll_y.pack(side="right", fill="y")
tree_inventario.configure(yscrollcommand=scroll_y.set)

scroll_x = ctk.CTkScrollbar(tree_frame, orientation="horizontal", command=tree_inventario.xview)
scroll_x.pack(side="bottom", fill="x")
tree_inventario.configure(xscrollcommand=scroll_x.set)

tree_inventario.pack(fill="both", expand=True)

# Configurar colores alternos para filas
style.configure("Treeview", 
                background="#2a2d2e",
                fieldbackground="#2a2d2e",
                foreground="white")
tree_inventario.tag_configure('oddrow', background="#2a2d2e")
tree_inventario.tag_configure('evenrow', background="#343638")

# Botones de inventario
btn_inv_frame = ctk.CTkFrame(frame_inventario)
btn_inv_frame.pack(pady=10)

btn_eliminar = ctk.CTkButton(btn_inv_frame, text="Eliminar Seleccionado", 
                            command=eliminar_producto_seleccionado, width=180)
btn_eliminar.pack(side="left", padx=10)

btn_detalles = ctk.CTkButton(btn_inv_frame, text="Ver Detalles", 
                            command=ver_detalles_producto, width=180)
btn_detalles.pack(side="left", padx=10)

# Foco inicial
entry_nombre.focus()

app.mainloop()