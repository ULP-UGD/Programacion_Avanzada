import customtkinter as ctk
from tkinter import messagebox
from datetime import date

class InformesTab(ctk.CTkFrame):
    def __init__(self, master, paciente_service, plan_service, app_controller):
        super().__init__(master)
        self.paciente_service = paciente_service
        self.plan_service = plan_service
        self.app_controller = app_controller

        self.pacientes_map = {} 

        self.pack(expand=True, fill="both")
        self._create_widgets()

    def _create_widgets(self):
        # --- Sección: Calcular Calorías Diarias por Paciente ---
        calc_frame = ctk.CTkFrame(self)
        calc_frame.pack(pady=10, padx=10, fill="x", anchor="n")
        
        ctk.CTkLabel(calc_frame, text="Calcular Calorías Diarias por Paciente:", font=("Arial", 14, "bold")).pack(pady=(0,10), anchor="w")

        selection_frame = ctk.CTkFrame(calc_frame) 
        selection_frame.pack(fill="x", pady=5)

        ctk.CTkLabel(selection_frame, text="Paciente:").pack(side="left", padx=(0,5))
        self.informe_paciente_combobox = ctk.CTkComboBox(selection_frame, width=250, state="readonly", values=["Cargando..."], command=self._informe_clear_result_on_change)
        self.informe_paciente_combobox.pack(side="left", padx=5)

        ctk.CTkLabel(selection_frame, text="Fecha (YYYY-MM-DD):").pack(side="left", padx=(10,5))
        self.informe_fecha_entry = ctk.CTkEntry(selection_frame, placeholder_text="YYYY-MM-DD", width=120)
        self.informe_fecha_entry.insert(0, date.today().isoformat())
        self.informe_fecha_entry.pack(side="left", padx=5)
        self.informe_fecha_entry.bind("<KeyRelease>", self._informe_clear_result_on_change) 

        self.calculate_calorias_button = ctk.CTkButton(selection_frame, text="📊 Calcular", command=self.calculate_daily_calories)
        self.calculate_calorias_button.pack(side="left", padx=10)

        self.calorias_result_label = ctk.CTkLabel(calc_frame, text="Resultado: -- kcal", font=("Arial", 16)) 
        self.calorias_result_label.pack(pady=5, anchor="w", padx=5)
        
        # --- Sección: Historial Completo de Comidas ---
        historial_main_frame = ctk.CTkFrame(self)
        historial_main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        header_frame = ctk.CTkFrame(historial_main_frame)
        header_frame.pack(fill="x", pady=(0,5))

        ctk.CTkLabel(header_frame, text="Historial Completo de Comidas Registradas:", font=("Arial", 14, "bold")).pack(side="left", anchor="w")
        
        self.refresh_historial_button = ctk.CTkButton(header_frame, text="🔄 Refrescar Historial", command=self.load_informes_data)
        self.refresh_historial_button.pack(side="right", anchor="ne")

        self.informe_text_area = ctk.CTkTextbox(historial_main_frame, wrap="word", state="disabled", font=("Courier New", 11), height=300)
        self.informe_text_area.pack(pady=5, fill="both", expand=True)

    def _informe_clear_result_on_change(self, event_or_value=None):
        """Limpia la etiqueta de resultado cuando cambia la selección o la fecha."""
        self.calorias_result_label.configure(text="Resultado: -- kcal")

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
                self.informe_paciente_combobox.configure(values=paciente_nombres_display)
                if paciente_nombres_display:
                    self.informe_paciente_combobox.set(paciente_nombres_display[0])
                else:
                    self.informe_paciente_combobox.set("No hay pacientes")
            else:
                self.informe_paciente_combobox.configure(values=[])
                self.informe_paciente_combobox.set("No hay pacientes")
        except Exception as e:
            self.informe_paciente_combobox.configure(values=[])
            self.informe_paciente_combobox.set("Error al cargar pacientes")
        self._informe_clear_result_on_change() 

    def calculate_daily_calories(self):
        paciente_display_name = self.informe_paciente_combobox.get()
        
        if paciente_display_name in ["Cargando...", "No hay pacientes", "Error al cargar pacientes"]:
            messagebox.showerror("Error de Selección", "Seleccione un paciente válido.", parent=self)
            self.calorias_result_label.configure(text="Resultado: Paciente no válido")
            return

        paciente_id = self.pacientes_map.get(paciente_display_name)
        if paciente_id is None:
            messagebox.showerror("Error Interno", "No se pudo obtener el ID del paciente seleccionado.", parent=self)
            self.calorias_result_label.configure(text="Resultado: Error ID Paciente")
            return

        fecha_str = self.informe_fecha_entry.get().strip()
        if not fecha_str:
            messagebox.showerror("Error de Formulario", "La fecha es obligatoria.", parent=self)
            self.calorias_result_label.configure(text="Resultado: Fecha no válida")
            return
            
        try:
            fecha_obj = date.fromisoformat(fecha_str)
        except ValueError:
            messagebox.showerror("Error de Formulario", "Formato de fecha incorrecto (YYYY-MM-DD).", parent=self)
            self.calorias_result_label.configure(text="Resultado: Fecha inválida")
            return
        
        try:
            calorias = self.plan_service.calcular_calorias_totales(paciente_id, fecha_obj)
            self.calorias_result_label.configure(text=f"Resultado: {calorias:.1f} kcal")
        except ValueError as ve: 
            messagebox.showerror("Error de Cálculo", str(ve), parent=self)
            self.calorias_result_label.configure(text="Resultado: Error")
        except Exception as e:
            messagebox.showerror("Error de Cálculo", f"No se pudieron calcular las calorías: {e}", parent=self)
            self.calorias_result_label.configure(text="Resultado: Error")

    def load_informes_data(self):
        """Carga el historial completo de comidas en el área de texto."""
        self.informe_text_area.configure(state="normal") 
        self.informe_text_area.delete("1.0", "end") 
        try:
            historial = self.plan_service.obtener_historial_completo()
            if not historial:
                self.informe_text_area.insert("end", "No hay registros de comidas en el sistema.")
            else:
                report_lines = []
                for plan_dict in historial:
                    calorias_comida = float(plan_dict['cantidad']) * float(plan_dict['calorias'])
                    line = (f"{plan_dict['fecha']}: {plan_dict['paciente_nombre']} comió {float(plan_dict['cantidad']):.2f} de "
                            f"{plan_dict['alimento_nombre']} ({calorias_comida:.1f} kcal)")
                    report_lines.append(line)
                self.informe_text_area.insert("end", "\n".join(report_lines))
        except Exception as e:
            self.informe_text_area.insert("end", f"Error al cargar el historial de comidas: {e}")
        self.informe_text_area.configure(state="disabled") 