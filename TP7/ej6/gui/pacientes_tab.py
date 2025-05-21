import customtkinter as ctk
from tkinter import ttk, messagebox 
import sqlite3 

class PacientesTab(ctk.CTkFrame):
    def __init__(self, master, paciente_service, app_controller):
        """
        Inicializa la pestaña de gestión de Pacientes.
        master: El frame de la pestaña padre (provisto por CTkTabview).
        paciente_service: Instancia del servicio de pacientes.
        app_controller: Instancia de la clase AppGUI principal para callbacks globales.
        """
        super().__init__(master)
        self.paciente_service = paciente_service
        self.app_controller = app_controller 

        self.pack(expand=True, fill="both") 

        self._create_widgets()
        self.load_pacientes()

    def _create_widgets(self):
        """Crea todos los widgets para la pestaña de pacientes."""
        
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=10, fill="x", anchor="n")

        ctk.CTkLabel(input_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.paciente_nombre_entry = ctk.CTkEntry(input_frame, width=250)
        self.paciente_nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.paciente_edad_entry = ctk.CTkEntry(input_frame, width=250)
        self.paciente_edad_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Peso (kg):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.paciente_peso_entry = ctk.CTkEntry(input_frame, width=250)
        self.paciente_peso_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        self.paciente_id_entry = ctk.CTkEntry(input_frame) 

        input_frame.columnconfigure(1, weight=1) 

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=5, padx=10, fill="x", anchor="n")

        self.add_paciente_button = ctk.CTkButton(button_frame, text="➕ Agregar", command=self.add_paciente)
        self.add_paciente_button.pack(side="left", padx=5, pady=5)
        
        self.update_paciente_button = ctk.CTkButton(button_frame, text="🔄 Actualizar", command=self.update_paciente)
        self.update_paciente_button.pack(side="left", padx=5, pady=5)

        self.delete_paciente_button = ctk.CTkButton(button_frame, text="🗑️ Eliminar", command=self.delete_paciente, fg_color="tomato")
        self.delete_paciente_button.pack(side="left", padx=5, pady=5)
        
        self.clear_paciente_fields_button = ctk.CTkButton(button_frame, text="✨ Limpiar", command=self.clear_paciente_fields)
        self.clear_paciente_fields_button.pack(side="left", padx=5, pady=5)

        tree_frame = ctk.CTkFrame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        columns = ("id", "nombre", "edad", "peso")
        self.pacientes_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        self.pacientes_tree.heading("id", text="ID")
        self.pacientes_tree.heading("nombre", text="Nombre")
        self.pacientes_tree.heading("edad", text="Edad")
        self.pacientes_tree.heading("peso", text="Peso (kg)")

        self.pacientes_tree.column("id", width=50, anchor="center", stretch=False)
        self.pacientes_tree.column("nombre", width=200, stretch=True)
        self.pacientes_tree.column("edad", width=70, anchor="center", stretch=False)
        self.pacientes_tree.column("peso", width=100, anchor="e", stretch=False)
        self.pacientes_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.pacientes_tree.yview)
        self.pacientes_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.pacientes_tree.bind("<<TreeviewSelect>>", self.on_paciente_select)

    def load_pacientes(self):
        """Carga o recarga los pacientes en el Treeview."""
        # Limpiar items existentes
        for item in self.pacientes_tree.get_children():
            self.pacientes_tree.delete(item)
        try:
            pacientes = self.paciente_service.obtener_todos()
            for p in pacientes:
                self.pacientes_tree.insert("", "end", values=(p.id, p.nombre, p.edad, f"{p.peso:.2f}"))
        except Exception as e:
            messagebox.showerror("Error al Cargar Pacientes", f"No se pudieron cargar los pacientes: {e}", parent=self)

    def on_paciente_select(self, event=None):
        """Se ejecuta cuando un paciente es seleccionado en el Treeview. Rellena los campos de entrada."""
        selected_item = self.pacientes_tree.focus() 
        if not selected_item:
            self.clear_paciente_fields()
            self.paciente_id_entry.delete(0, "end")
            return
        
        values = self.pacientes_tree.item(selected_item, "values")
        self.clear_paciente_fields() 
        
        self.paciente_id_entry.delete(0, "end") 
        self.paciente_id_entry.insert(0, values[0]) 
        
        self.paciente_nombre_entry.insert(0, values[1])
        self.paciente_edad_entry.insert(0, values[2])   
        self.paciente_peso_entry.insert(0, values[3])  

    def clear_paciente_fields(self):
        """Limpia los campos de entrada de paciente y la selección del Treeview."""
        self.paciente_id_entry.delete(0, "end") 
        self.paciente_nombre_entry.delete(0, "end")
        self.paciente_edad_entry.delete(0, "end")
        self.paciente_peso_entry.delete(0, "end")
        
        if self.pacientes_tree.focus(): 
            self.pacientes_tree.selection_remove(self.pacientes_tree.focus())

    def add_paciente(self):
        """Agrega un nuevo paciente usando los datos de los campos de entrada."""
        nombre = self.paciente_nombre_entry.get().strip()
        edad_str = self.paciente_edad_entry.get().strip()
        peso_str = self.paciente_peso_entry.get().strip()

        if not nombre or not edad_str or not peso_str:
            messagebox.showerror("Error de Formulario", "Todos los campos (Nombre, Edad, Peso) son obligatorios.", parent=self)
            return
        try:
            edad = int(edad_str)
            peso = float(peso_str)
        except ValueError:
            messagebox.showerror("Error de Formulario", "Edad debe ser un número entero y Peso debe ser un número.", parent=self)
            return
        
        try:
            self.paciente_service.crear_paciente(nombre, edad, peso)
            messagebox.showinfo("Éxito", "Paciente agregado correctamente.", parent=self)
            self.load_pacientes() 
            self.clear_paciente_fields() 
            self.app_controller.refresh_dependent_views_after_data_change() 
        except ValueError as ve: 
            messagebox.showerror("Error de Validación de Negocio", str(ve), parent=self)
        except Exception as e: 
            messagebox.showerror("Error de Creación", f"No se pudo agregar el paciente: {e}", parent=self)

    def update_paciente(self):
        """Actualiza un paciente existente."""
        paciente_id_str = self.paciente_id_entry.get()
        if not paciente_id_str:
            messagebox.showerror("Error", "Seleccione un paciente de la lista para actualizar.", parent=self)
            return
        
        nombre = self.paciente_nombre_entry.get().strip()
        edad_str = self.paciente_edad_entry.get().strip()
        peso_str = self.paciente_peso_entry.get().strip()

        # Validación básica de UI
        if not nombre or not edad_str or not peso_str:
            messagebox.showerror("Error de Formulario", "Todos los campos (Nombre, Edad, Peso) son obligatorios.", parent=self)
            return
        try:
            paciente_id = int(paciente_id_str)
            edad = int(edad_str)
            peso = float(peso_str)
        except ValueError:
            messagebox.showerror("Error de Formulario", "ID y Edad deben ser enteros, Peso debe ser un número.", parent=self)
            return
             
        paciente_obj_para_actualizar = self.paciente_service.obtener_por_id(paciente_id)
        if not paciente_obj_para_actualizar:
             messagebox.showerror("Error", f"No se encontró el paciente con ID {paciente_id} para actualizar.", parent=self)
             self.clear_paciente_fields() 
             self.load_pacientes() 
             return

        paciente_obj_para_actualizar.nombre = nombre
        paciente_obj_para_actualizar.edad = edad
        paciente_obj_para_actualizar.peso = peso
        
        try:
            if self.paciente_service.actualizar_paciente(paciente_obj_para_actualizar):
                 messagebox.showinfo("Éxito", "Paciente actualizado correctamente.", parent=self)
                 self.load_pacientes()
                 self.clear_paciente_fields()
                 self.app_controller.refresh_dependent_views_after_data_change()
            else:
                messagebox.showerror("Error de Actualización", "No se pudo actualizar el paciente (posiblemente no encontrado en BD).", parent=self)
        except ValueError as ve: 
            messagebox.showerror("Error de Validación de Negocio", str(ve), parent=self)
        except Exception as e:
            messagebox.showerror("Error de Actualización", f"No se pudo actualizar el paciente: {e}", parent=self)

    def delete_paciente(self):
        """Elimina el paciente seleccionado."""
        paciente_id_str = self.paciente_id_entry.get()
        if not paciente_id_str:
            messagebox.showerror("Error", "Seleccione un paciente de la lista para eliminar.", parent=self)
            return
        
        # Confirmación
        if not messagebox.askyesno("Confirmar Eliminación",
                                   "¿Está seguro de que desea eliminar este paciente?\n"
                                   "Todos sus registros de comidas asociadas también serán eliminados (ON DELETE CASCADE).",
                                   parent=self):
            return
        try:
            paciente_id = int(paciente_id_str)
            if self.paciente_service.eliminar_paciente(paciente_id):
                messagebox.showinfo("Éxito", "Paciente eliminado correctamente.", parent=self)
                self.load_pacientes()
                self.clear_paciente_fields()
                self.app_controller.refresh_dependent_views_after_data_change() 
            else:
                messagebox.showerror("Error de Eliminación", "No se pudo eliminar el paciente (no encontrado).", parent=self)
        except ValueError as ve: 
             messagebox.showerror("Error de Validación", str(ve), parent=self)
        except sqlite3.IntegrityError as ie: 
            messagebox.showerror("Error de Integridad", f"No se pudo eliminar el paciente debido a restricciones de la base de datos: {ie}", parent=self)
        except Exception as e:
            messagebox.showerror("Error de Eliminación", f"No se pudo eliminar el paciente: {e}", parent=self)