import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3 

class AlimentosTab(ctk.CTkFrame):
    def __init__(self, master, alimento_service, app_controller):
        """
        Inicializa la pestaña de gestión de Alimentos.
        master: El frame de la pestaña padre (provisto por CTkTabview).
        alimento_service: Instancia del servicio de alimentos.
        app_controller: Instancia de la clase AppGUI principal para callbacks globales.
        """
        super().__init__(master)
        self.alimento_service = alimento_service
        self.app_controller = app_controller

        self.pack(expand=True, fill="both")

        self._create_widgets()
        self.load_alimentos()

    def _create_widgets(self):
        """Crea todos los widgets para la pestaña de alimentos."""

        # Frame para campos de entrada
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=10, fill="x", anchor="n")

        ctk.CTkLabel(input_frame, text="Nombre Alimento:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.alimento_nombre_entry = ctk.CTkEntry(input_frame, width=250)
        self.alimento_nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Calorías (por porción/unidad):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.alimento_calorias_entry = ctk.CTkEntry(input_frame, width=250)
        self.alimento_calorias_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        self.alimento_id_entry = ctk.CTkEntry(input_frame) 

        input_frame.columnconfigure(1, weight=1)

        # Frame para botones
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=5, padx=10, fill="x", anchor="n")

        self.add_alimento_button = ctk.CTkButton(button_frame, text="➕ Agregar", command=self.add_alimento)
        self.add_alimento_button.pack(side="left", padx=5, pady=5)
        
        self.update_alimento_button = ctk.CTkButton(button_frame, text="🔄 Actualizar", command=self.update_alimento)
        self.update_alimento_button.pack(side="left", padx=5, pady=5)

        self.delete_alimento_button = ctk.CTkButton(button_frame, text="🗑️ Eliminar", command=self.delete_alimento, fg_color="tomato")
        self.delete_alimento_button.pack(side="left", padx=5, pady=5)
        
        self.clear_alimento_fields_button = ctk.CTkButton(button_frame, text="✨ Limpiar", command=self.clear_alimento_fields)
        self.clear_alimento_fields_button.pack(side="left", padx=5, pady=5)

        # Frame para el Treeview
        tree_frame = ctk.CTkFrame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        columns = ("id", "nombre", "calorias")
        self.alimentos_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        self.alimentos_tree.heading("id", text="ID")
        self.alimentos_tree.heading("nombre", text="Nombre Alimento")
        self.alimentos_tree.heading("calorias", text="Calorías")

        self.alimentos_tree.column("id", width=50, anchor="center", stretch=False)
        self.alimentos_tree.column("nombre", width=200, stretch=True)
        self.alimentos_tree.column("calorias", width=100, anchor="e", stretch=False)
        
        self.alimentos_tree.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.alimentos_tree.yview)
        self.alimentos_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.alimentos_tree.bind("<<TreeviewSelect>>", self.on_alimento_select)

    def load_alimentos(self):
        """Carga o recarga los alimentos en el Treeview."""
        for item in self.alimentos_tree.get_children():
            self.alimentos_tree.delete(item)
        try:
            alimentos = self.alimento_service.obtener_todos()
            for a in alimentos:
                self.alimentos_tree.insert("", "end", values=(a.id, a.nombre, f"{a.calorias:.1f}"))
        except Exception as e:
            messagebox.showerror("Error al Cargar Alimentos", f"No se pudieron cargar los alimentos: {e}", parent=self)

    def on_alimento_select(self, event=None):
        """Se ejecuta cuando un alimento es seleccionado. Rellena los campos."""
        selected_item = self.alimentos_tree.focus()
        if not selected_item:
            self.clear_alimento_fields()
            self.alimento_id_entry.delete(0, "end")
            return
        
        values = self.alimentos_tree.item(selected_item, "values")
        self.clear_alimento_fields()
        
        self.alimento_id_entry.delete(0, "end")
        self.alimento_id_entry.insert(0, values[0]) # ID
        
        self.alimento_nombre_entry.insert(0, values[1])    # Nombre
        self.alimento_calorias_entry.insert(0, values[2]) # Calorías

    def clear_alimento_fields(self):
        """Limpia los campos de entrada de alimento y la selección del Treeview."""
        self.alimento_id_entry.delete(0, "end")
        self.alimento_nombre_entry.delete(0, "end")
        self.alimento_calorias_entry.delete(0, "end")
        if self.alimentos_tree.focus():
            self.alimentos_tree.selection_remove(self.alimentos_tree.focus())

    def add_alimento(self):
        """Agrega un nuevo alimento."""
        nombre = self.alimento_nombre_entry.get().strip()
        calorias_str = self.alimento_calorias_entry.get().strip()

        if not nombre or not calorias_str:
            messagebox.showerror("Error de Formulario", "Nombre y Calorías son obligatorios.", parent=self)
            return
        try:
            calorias = float(calorias_str)
        except ValueError:
            messagebox.showerror("Error de Formulario", "Calorías debe ser un número.", parent=self)
            return
        
        try:
            self.alimento_service.crear_alimento(nombre, calorias) 
            messagebox.showinfo("Éxito", "Alimento agregado correctamente.", parent=self)
            self.load_alimentos()
            self.clear_alimento_fields()
            self.app_controller.refresh_dependent_views_after_data_change()
        except ValueError as ve:
            messagebox.showerror("Error de Validación de Negocio", str(ve), parent=self)
        except Exception as e:
            messagebox.showerror("Error de Creación", f"No se pudo agregar el alimento: {e}", parent=self)

    def update_alimento(self):
        """Actualiza un alimento existente."""
        alimento_id_str = self.alimento_id_entry.get()
        if not alimento_id_str:
            messagebox.showerror("Error", "Seleccione un alimento de la lista para actualizar.", parent=self)
            return
        
        nombre = self.alimento_nombre_entry.get().strip()
        calorias_str = self.alimento_calorias_entry.get().strip()

        if not nombre or not calorias_str:
            messagebox.showerror("Error de Formulario", "Nombre y Calorías son obligatorios.", parent=self)
            return
        try:
            alimento_id = int(alimento_id_str)
            calorias = float(calorias_str)
        except ValueError:
            messagebox.showerror("Error de Formulario", "ID debe ser entero, Calorías debe ser un número.", parent=self)
            return

        alimento_obj_actualizar = self.alimento_service.obtener_por_id(alimento_id)
        if not alimento_obj_actualizar:
            messagebox.showerror("Error", f"No se encontró el alimento con ID {alimento_id} para actualizar.", parent=self)
            self.clear_alimento_fields()
            self.load_alimentos()
            return
            
        alimento_obj_actualizar.nombre = nombre
        alimento_obj_actualizar.calorias = calorias
        
        try:
            if self.alimento_service.actualizar_alimento(alimento_obj_actualizar):
                 messagebox.showinfo("Éxito", "Alimento actualizado correctamente.", parent=self)
                 self.load_alimentos()
                 self.clear_alimento_fields()
                 self.app_controller.refresh_dependent_views_after_data_change()
            else:
                messagebox.showerror("Error de Actualización", "No se pudo actualizar el alimento.", parent=self)
        except ValueError as ve:
            messagebox.showerror("Error de Validación de Negocio", str(ve), parent=self)
        except Exception as e:
            messagebox.showerror("Error de Actualización", f"No se pudo actualizar el alimento: {e}", parent=self)

    def delete_alimento(self):
        """Elimina el alimento seleccionado."""
        alimento_id_str = self.alimento_id_entry.get()
        if not alimento_id_str:
            messagebox.showerror("Error", "Seleccione un alimento de la lista para eliminar.", parent=self)
            return
        
        if not messagebox.askyesno("Confirmar Eliminación",
                                   "¿Está seguro de que desea eliminar este alimento?\n"
                                   "No podrá ser eliminado si está siendo utilizado en algún plan de comidas (ON DELETE RESTRICT).",
                                   parent=self):
            return
        try:
            alimento_id = int(alimento_id_str)
            if self.alimento_service.eliminar_alimento(alimento_id):
                messagebox.showinfo("Éxito", "Alimento eliminado correctamente.", parent=self)
                self.load_alimentos()
                self.clear_alimento_fields()
                self.app_controller.refresh_dependent_views_after_data_change()
            else:
                messagebox.showerror("Error de Eliminación", "No se pudo eliminar el alimento (no encontrado).", parent=self)
        except ValueError as ve:
             messagebox.showerror("Error de Validación", str(ve), parent=self)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error de Integridad", "No se puede eliminar el alimento porque está referenciado en planes de comida.", parent=self)
        except Exception as e:
            messagebox.showerror("Error de Eliminación", f"No se pudo eliminar el alimento: {e}", parent=self)

    def update_alimento_combobox_from_service(self):

        print(f"AlimentosTab: update_alimento_combobox_from_service llamado (actualmente no hace nada específico para esta tab)")
        pass