from datetime import date, timedelta
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


def inicializar_datos(paciente_service: PacienteService, alimento_service: AlimentoService, plan_service: PlanComidaService):
    """Función para inicializar datos de prueba"""
    # Crear pacientes
    paciente1 = paciente_service.crear_paciente("Juan Pérez", 35, 78.5)
    paciente2 = paciente_service.crear_paciente("María Gómez", 28, 62.3)

    # Crear alimentos
    manzana = alimento_service.crear_alimento("Manzana", 52.0)
    pollo = alimento_service.crear_alimento("Pollo asado", 165.0)
    arroz = alimento_service.crear_alimento("Arroz integral", 130.0)
    salmon = alimento_service.crear_alimento("Salmón", 208.0)

    # Registrar comidas
    hoy = date.today()
    ayer = hoy - timedelta(days=1)

    # Comidas para hoy
    plan_service.registrar_comida(
        paciente1.id, manzana.id, hoy, 2.0)  # 2 manzanas
    plan_service.registrar_comida(
        paciente1.id, pollo.id, hoy, 0.3)    # 300g de pollo
    plan_service.registrar_comida(
        paciente2.id, arroz.id, hoy, 0.2)    # 200g de arroz

    # Comidas para ayer
    plan_service.registrar_comida(
        paciente1.id, salmon.id, ayer, 0.25)  # 250g de salmón
    plan_service.registrar_comida(
        paciente2.id, manzana.id, ayer, 1.5)  # 1.5 manzanas


def mostrar_estadisticas(paciente_service: PacienteService, alimento_service: AlimentoService, plan_service: PlanComidaService):
    """Muestra estadísticas de los datos registrados"""
    print("\n=== Pacientes Registrados ===")
    for paciente in paciente_service.obtener_todos():
        print(paciente)

    print("\n=== Alimentos Registrados ===")
    for alimento in alimento_service.obtener_todos():
        print(alimento)

    print("\n=== Planes de Comida ===")
    for plan in plan_service.obtener_historial_completo():
        print(f"{plan['paciente_nombre']} comió {plan['cantidad']} de {plan['alimento_nombre']} "
              f"el {plan['fecha']} ({plan['calorias'] * plan['cantidad']:.1f} kcal)")


def main():
    # Configuración inicial
    db_config = DatabaseConfig()
    tm = TransactionManager(db_config)

    # Inicializar repositorios
    paciente_repo = PacienteRepository(tm)
    alimento_repo = AlimentoRepository(tm)
    plan_repo = PlanComidaRepository(tm)

    # Inicializar servicios
    paciente_service = PacienteService(paciente_repo)
    alimento_service = AlimentoService(alimento_repo)
    plan_service = PlanComidaService(plan_repo, paciente_repo, alimento_repo)

    # Inicializar datos de prueba
    inicializar_datos(paciente_service, alimento_service, plan_service)

    # Mostrar datos registrados
    mostrar_estadisticas(paciente_service, alimento_service, plan_service)

    # Mostrar calorías consumidas hoy por el primer paciente
    pacientes = paciente_service.obtener_todos()
    if pacientes:
        hoy = date.today()
        calorias = plan_service.calcular_calorias_totales(pacientes[0].id, hoy)
        print(f"\n{pacientes[0].nombre} consumió {calorias:.1f} kcal hoy")


if __name__ == "__main__":
    main()