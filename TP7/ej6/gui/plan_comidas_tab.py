import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import date
import sqlite3

class PlanComidasTab(ctk.CTkFrame):
    def __init__(self, master, paciente_service, alimento_service, plan_service, app_controller):
        super().__init__(master)
        self.paciente_service = paciente_service
        self.alimento_service = alimento_service
        self.plan_service = plan_service
        self.app_controller = app_controller

        self.pacientes_map = {} 
        self.alimentos_map = {} 

        self.pack(expand=True, fill="both")
        self._create_widgets()

    def _create_widgets(self):
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=10, fill="x", anchor="n")

        ctk.CTkLabel(input_frame, text="Paciente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.plan_paciente_combobox = ctk.CTkComboBox(input_frame, width=250, state="readonly", values=["Cargando..."])
        self.plan_paciente_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Alimento:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.plan_alimento_combobox = ctk.CTkComboBox(input_frame, width=250, state="readonly", values=["Cargando..."])
        self.plan_alimento_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.plan_fecha_entry = ctk.CTkEntry(input_frame, placeholder_text="YYYY-MM-DD", width=250)
        self.plan_fecha_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.plan_fecha_entry.insert(0, date.today().isoformat()) # Fecha de hoy por defecto

        ctk.CTkLabel(input_frame, text="Cantidad:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.plan_cantidad_entry = ctk.CTkEntry(input_frame, placeholder_text="Ej: 1.5 o 100 (gramos)", width=250)
        self.plan_cantidad_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        self.plan_id_entry = ctk.CTkEntry(input_frame) # Oculto, para ID del plan
        input_frame.columnconfigure(1, weight=1)

        # --- Frame de Botones ---
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=5, padx=10, fill="x", anchor="n")

        self.add_plan_button = ctk.CTkButton(button_frame, text="📝 Registrar Comida", command=self.add_plan_comida)
        self.add_plan_button.pack(side="left", padx=5, pady=5)
        
        self.delete_plan_button = ctk.CTkButton(button_frame, text="🗑️ Eliminar Registro", command=self.delete_plan_comida, fg_color="tomato")
        self.delete_plan_button.pack(side="left", padx=5, pady=5)

        self.clear_plan_fields_button = ctk.CTkButton(button_frame, text="✨ Limpiar Campos", command=self.clear_plan_fields)
        self.clear_plan_fields_button.pack(side="left", padx=5, pady=5)
        
        # --- Frame del Treeview ---
        tree_frame = ctk.CTkFrame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        columns = ("plan_id", "fecha", "paciente", "alimento", "cantidad", "calorias_total")
        self.plan_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        self.plan_tree.heading("plan_id", text="ID Plan")
        self.plan_tree.heading("fecha", text="Fecha")
        self.plan_tree.heading("paciente", text="Paciente")
        self.plan_tree.heading("alimento", text="Alimento")
        self.plan_tree.heading("cantidad", text="Cantidad")
        self.plan_tree.heading("calorias_total", text="Kcal Registro")

        self.plan_tree.column("plan_id", width=60, anchor="center", stretch=False)
        self.plan_tree.column("fecha", width=100, anchor="center", stretch=False)
        self.plan_tree.column("paciente", width=150, stretch=True)
        self.plan_tree.column("alimento", width=150, stretch=True)
        self.plan_tree.column("cantidad", width=80, anchor="e", stretch=False)
        self.plan_tree.column("calorias_total", width=100, anchor="e", stretch=False)

        self.plan_tree.pack(side="left", fill="both", expand=True)
        scrollbar_plan = ttk.Scrollbar(tree_frame, orient="vertical", command=self.plan_tree.yview)
        self.plan_tree.configure(yscrollcommand=scrollbar_plan.set)
        scrollbar_plan.pack(side="right", fill="y")

        self.plan_tree.bind("<<TreeviewSelect>>", self.on_plan_select)

    def update_paciente_combobox_from_service(self):
        self.pacientes_map.clear()
        try:
            pacientes = self.paciente_service.obtener_todos()
            paciente_nombres_display = []
            if pacientes:
                for p in pacientes:
                    display_name = f"{p.nombre} (ID: {p.id})"
                    self.pacientes_map[display_name] = p.id
                    paciente_nombres_display.append(display_name)
                self.plan_paciente_combobox.configure(values=paciente_nombres_display)
                if paciente_nombres_display:
                    self.plan_paciente_combobox.set(paciente_nombres_display[0])
                else:
                    self.plan_paciente_combobox.set("No hay pacientes")
            else:
                self.plan_paciente_combobox.configure(values=[])
                self.plan_paciente_combobox.set("No hay pacientes")
        except Exception as e:
            self.plan_paciente_combobox.configure(values=[])
            self.plan_paciente_combobox.set("Error al cargar pacientes")

    def update_alimento_combobox_from_service(self):
        self.alimentos_map.clear()
        try:
            alimentos = self.alimento_service.obtener_todos()
            alimento_nombres_display = []
            if alimentos:
                for a in alimentos:
                    display_name = f"{a.nombre} ({a.calorias:.0f} kcal)"
                    self.alimentos_map[display_name] = a.id
                    alimento_nombres_display.append(display_name)
                self.plan_alimento_combobox.configure(values=alimento_nombres_display)
                if alimento_nombres_display:
                    self.plan_alimento_combobox.set(alimento_nombres_display[0])
                else:
                     self.plan_alimento_combobox.set("No hay alimentos")
            else:
                self.plan_alimento_combobox.configure(values=[])
                self.plan_alimento_combobox.set("No hay alimentos")
        except Exception as e:
            self.plan_alimento_combobox.configure(values=[])
            self.plan_alimento_combobox.set("Error al cargar alimentos")

    def load_plan_comidas(self):
        for item in self.plan_tree.get_children():
            self.plan_tree.delete(item)
        try:
            planes_data = self.plan_service.obtener_historial_completo() 
            for plan_dict in planes_data:
                calorias_registro = float(plan_dict['cantidad']) * float(plan_dict['calorias'])
                self.plan_tree.insert("", "end", values=(
                    plan_dict['id'],
                    plan_dict['fecha'],
                    plan_dict['paciente_nombre'],
                    plan_dict['alimento_nombre'],
                    f"{float(plan_dict['cantidad']):.2f}", 
                    f"{calorias_registro:.1f}"
                ))
        except Exception as e:
            messagebox.showerror("Error al Cargar Planes", f"No se pudieron cargar los planes de comida: {e}", parent=self)

    def on_plan_select(self, event=None):
        selected_item = self.plan_tree.focus()
        if not selected_item:
            self.plan_id_entry.delete(0, "end")
            return
        
        values = self.plan_tree.item(selected_item, "values")
        self.plan_id_entry.delete(0, "end") 
        self.plan_id_entry.insert(0, values[0]) 

    def clear_plan_fields(self):
        self.plan_id_entry.delete(0, "end")
        self.plan_cantidad_entry.delete(0, "end")
        self.plan_fecha_entry.delete(0, "end")
        self.plan_fecha_entry.insert(0, date.today().isoformat()) 
        
        if self.plan_paciente_combobox.cget("values") and self.plan_paciente_combobox.cget("values")[0] not in ["Cargando...", "No hay pacientes", "Error al cargar pacientes"]:
            self.plan_paciente_combobox.set(self.plan_paciente_combobox.cget("values")[0])
        if self.plan_alimento_combobox.cget("values") and self.plan_alimento_combobox.cget("values")[0] not in ["Cargando...", "No hay alimentos", "Error al cargar alimentos"]:
            self.plan_alimento_combobox.set(self.plan_alimento_combobox.cget("values")[0])
            
        if self.plan_tree.focus():
            self.plan_tree.selection_remove(self.plan_tree.focus())

    def add_plan_comida(self):
        paciente_display_name = self.plan_paciente_combobox.get()
        alimento_display_name = self.plan_alimento_combobox.get()

        if paciente_display_name in ["Cargando...", "No hay pacientes", "Error al cargar pacientes"]:
            messagebox.showerror("Error de Selección", "Seleccione un paciente válido.", parent=self)
            return
        if alimento_display_name in ["Cargando...", "No hay alimentos", "Error al cargar alimentos"]:
            messagebox.showerror("Error de Selección", "Seleccione un alimento válido.", parent=self)
            return

        paciente_id = self.pacientes_map.get(paciente_display_name)
        alimento_id = self.alimentos_map.get(alimento_display_name)

        if paciente_id is None or alimento_id is None:
            messagebox.showerror("Error Interno", "No se pudo obtener el ID del paciente o alimento seleccionado.", parent=self)
            return

        fecha_str = self.plan_fecha_entry.get().strip()
        cantidad_str = self.plan_cantidad_entry.get().strip()

        if not fecha_str or not cantidad_str:
            messagebox.showerror("Error de Formulario", "Fecha y Cantidad son obligatorios.", parent=self)
            return
        
        try:
            fecha_obj = date.fromisoformat(fecha_str)
            cantidad = float(cantidad_str)
        except ValueError:
            messagebox.showerror("Error de Formulario", "Formato de fecha incorrecto (YYYY-MM-DD) o cantidad no numérica.", parent=self)
            return
        
        try:
            self.plan_service.registrar_comida(paciente_id, alimento_id, fecha_obj, cantidad)
            messagebox.showinfo("Éxito", "Comida registrada correctamente.", parent=self)
            self.load_plan_comidas()
            self.clear_plan_fields()
            self.app_controller.refresh_dependent_views_after_data_change() 
        except ValueError as ve:
            messagebox.showerror("Error de Validación de Negocio", str(ve), parent=self)
        except Exception as e:
            messagebox.showerror("Error de Registro", f"No se pudo registrar la comida: {e}", parent=self)

    def delete_plan_comida(self):
        plan_id_str = self.plan_id_entry.get()
        if not plan_id_str:
            messagebox.showerror("Error", "Seleccione un registro de comida de la lista para eliminar.", parent=self)
            return
        
        if not messagebox.askyesno("Confirmar Eliminación",
                                   "¿Está seguro de que desea eliminar este registro de comida?",
                                   parent=self):
            return
        try:
            plan_id = int(plan_id_str)
            if self.plan_service.eliminar_registro_comida(plan_id):
                messagebox.showinfo("Éxito", "Registro de comida eliminado correctamente.", parent=self)
                self.load_plan_comidas()
                self.plan_id_entry.delete(0, "end")
                self.app_controller.refresh_dependent_views_after_data_change() 
            else:
                messagebox.showerror("Error de Eliminación", "No se pudo eliminar el registro (no encontrado).", parent=self)
        except ValueError as ve:
            messagebox.showerror("Error de Validación", str(ve), parent=self)
        except Exception as e:
            messagebox.showerror("Error de Eliminación", f"No se pudo eliminar el registro: {e}", parent=self)