from datetime import date
from typing import Any, List, Dict, Optional
from models import PlanComida

class PlanComidaService:
    def __init__(self, plan_repo, paciente_repo, alimento_repo):
        self.plan_repo = plan_repo
        self.paciente_repo = paciente_repo
        self.alimento_repo = alimento_repo

    def registrar_comida(self, paciente_id: int, alimento_id: int,
                         fecha: date, cantidad: float) -> Optional[int]:
        # Validaciones básicas
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        paciente = self.paciente_repo.get_by_id(paciente_id)
        if not paciente:
            raise ValueError("Paciente no encontrado")

        alimento = self.alimento_repo.get_by_id(alimento_id)
        if not alimento:
            raise ValueError("Alimento no encontrado")

        # Crear y guardar el plan
        plan = PlanComida(paciente_id, alimento_id, fecha, cantidad)
        return self.plan_repo.add(plan)

    def obtener_historial_completo(self) -> List[Dict[str, Any]]:
        return self.plan_repo.get_all()

    def obtener_historial_paciente(self, paciente_id: int) -> List[Dict[str, Any]]:
        return self.plan_repo.get_by_paciente(paciente_id)

    def obtener_por_fecha(self, fecha: date) -> List[Dict[str, Any]]:
        return self.plan_repo.get_by_fecha(fecha)

    def eliminar_registro_comida(self, plan_id: int) -> bool:
        return self.plan_repo.delete(plan_id)

    def calcular_calorias_totales(self, paciente_id: int, fecha: date) -> float:
        registros = self.plan_repo.get_by_paciente(paciente_id)
        total = 0.0
        for registro in registros:
            if date.fromisoformat(registro['fecha']) == fecha:
                total += registro['cantidad'] * registro['calorias']
        return total