import sys
import os
from datetime import date, timedelta 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

from config import DatabaseConfig, TransactionManager
from repositories import (
    PacienteRepository,
    AlimentoRepository,
    PlanComidaRepository
)
from services import (
    PacienteService,
    AlimentoService,
    PlanComidaService
)
from gui.app_gui import AppGUI 

def inicializar_datos_de_prueba(paciente_service: PacienteService, alimento_service: AlimentoService, plan_service: PlanComidaService):
    """Función para inicializar datos de prueba si la base de datos está vacía."""
    print("Verificando si se necesitan datos de prueba...")
    try:
        # Solo inicializar si no hay pacientes Y no hay alimentos
        if not paciente_service.obtener_todos() and not alimento_service.obtener_todos():
            print("Base de datos vacía. Inicializando datos de prueba...")
            # Crear pacientes
            paciente1 = paciente_service.crear_paciente("Juan Pérez", 35, 78.5)
            paciente2 = paciente_service.crear_paciente("María Gómez", 28, 62.3)
            print(f"Creado: {paciente1}")
            print(f"Creado: {paciente2}")

            # Crear alimentos
            manzana = alimento_service.crear_alimento("Manzana", 52.0)
            pollo = alimento_service.crear_alimento("Pollo asado", 165.0)
            arroz = alimento_service.crear_alimento("Arroz integral", 130.0)
            salmon = alimento_service.crear_alimento("Salmón", 208.0)
            print(f"Creado: {manzana}")
            print(f"Creado: {pollo}")
            print(f"Creado: {arroz}")
            print(f"Creado: {salmon}")

            # Registrar comidas
            hoy = date.today()
            ayer = hoy - timedelta(days=1)

            plan_service.registrar_comida(paciente1.id, manzana.id, hoy, 2.0)
            plan_service.registrar_comida(paciente1.id, pollo.id, hoy, 0.3)
            plan_service.registrar_comida(paciente2.id, arroz.id, hoy, 0.2)
            plan_service.registrar_comida(paciente1.id, salmon.id, ayer, 0.25)
            plan_service.registrar_comida(paciente2.id, manzana.id, ayer, 1.5)
            print("Comidas de prueba registradas.")
            print("Datos de prueba inicializados exitosamente.")
        else:
            print("La base de datos ya contiene datos. No se inicializaron datos de prueba.")
    except Exception as e:
        print(f"Error durante la inicialización de datos de prueba: {e}")


def main_gui():
    """Configura e inicia la aplicación GUI."""

    db_name = "nutricionista.db"
    db_path = os.path.join(SCRIPT_DIR, db_name) 
  
    print(f"Usando base de datos en: {db_path}")

    db_config = DatabaseConfig(db_path=db_path)


    tm = TransactionManager(db_config)

    # --- Inicialización de Repositorios ---
    paciente_repo = PacienteRepository(tm)
    alimento_repo = AlimentoRepository(tm)
    plan_repo = PlanComidaRepository(tm)

    # --- Inicialización de Servicios ---
    paciente_service = PacienteService(paciente_repo)
    alimento_service = AlimentoService(alimento_repo)
    plan_service = PlanComidaService(plan_repo, paciente_repo, alimento_repo)
    
    # --- Opcional: Inicializar datos de prueba ---
    inicializar_datos_de_prueba(paciente_service, alimento_service, plan_service)

    # --- Crear e Iniciar la Aplicación GUI ---
    app = AppGUI(paciente_service, alimento_service, plan_service)
    app.mainloop()

if __name__ == "__main__":
    main_gui()
