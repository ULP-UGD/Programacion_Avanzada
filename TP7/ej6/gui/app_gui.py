import customtkinter as ctk
from tkinter import messagebox
from datetime import date
import sqlite3

from .pacientes_tab import PacientesTab
from .alimentos_tab import AlimentosTab 
from .plan_comidas_tab import PlanComidasTab 
from .informes_tab import InformesTab 

class AppGUI(ctk.CTk):
    def __init__(self, paciente_service, alimento_service, plan_service):
        super().__init__()
        self.paciente_service = paciente_service
        self.alimento_service = alimento_service
        self.plan_service = plan_service

        self.title("Software Nutricionista 🍎")
        self.geometry("1100x750")


        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.tab_view = ctk.CTkTabview(self, anchor="nw")
        self.tab_view.pack(expand=True, fill="both", padx=10, pady=10)

        # Crear las pestañas físicas
        tab_p_frame = self.tab_view.add("Pacientes")
        tab_a_frame = self.tab_view.add("Alimentos")
        tab_pc_frame = self.tab_view.add("Plan Comidas")
        tab_i_frame = self.tab_view.add("Informes")

        self.pacientes_tab_ui = PacientesTab(tab_p_frame, self.paciente_service, self)
        
        self.alimentos_tab_ui = AlimentosTab(tab_a_frame, self.alimento_service, self)
        self.plan_comidas_tab_ui = PlanComidasTab(tab_pc_frame, self.paciente_service, self.alimento_service, self.plan_service, self)
        self.informes_tab_ui = InformesTab(tab_i_frame, self.paciente_service, self.plan_service, self)
        
        self.refresh_dependent_views_after_data_change(initial_load=True)


    def refresh_dependent_views_after_data_change(self, initial_load=False):
        """
        Llama a los métodos de actualización en las pestañas relevantes.
        Se usa después de agregar/editar/eliminar datos en una pestaña
        para asegurar que otras pestañas que dependen de esos datos (ej. ComboBoxes)
        se actualicen.
        `initial_load` se puede usar para diferenciar la primera carga.
        """
        print("AppGUI: Refrescando vistas dependientes...")

        # Actualizar ComboBox de pacientes en la pestaña de Plan de Comidas y Informes
        if hasattr(self.plan_comidas_tab_ui, 'update_paciente_combobox_from_service'):
            self.plan_comidas_tab_ui.update_paciente_combobox_from_service()
        if hasattr(self.informes_tab_ui, 'update_paciente_combobox_from_service'):
            self.informes_tab_ui.update_paciente_combobox_from_service()

        # Actualizar ComboBox de alimentos en la pestaña de Plan de Comidas
        if hasattr(self.plan_comidas_tab_ui, 'update_alimento_combobox_from_service'):
            self.plan_comidas_tab_ui.update_alimento_combobox_from_service()

        # Recargar datos en la pestaña de Plan de Comidas (Treeview)
        if hasattr(self.plan_comidas_tab_ui, 'load_plan_comidas'):
            self.plan_comidas_tab_ui.load_plan_comidas()
            
        # Recargar datos en la pestaña de Informes (Textbox)
        if hasattr(self.informes_tab_ui, 'load_informes_data'):
            self.informes_tab_ui.load_informes_data()            