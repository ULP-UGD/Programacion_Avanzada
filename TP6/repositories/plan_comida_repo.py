from datetime import date
from typing import List, Optional, Dict, Any
from models import PlanComida

class PlanComidaRepository:
    def __init__(self, transaction_manager):
        self.tm = transaction_manager

    def add(self, plan: PlanComida) -> int:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                """INSERT INTO plan_comidas 
                (paciente_id, alimento_id, fecha, cantidad) 
                VALUES (?, ?, ?, ?);""",
                (plan.paciente_id, plan.alimento_id,
                 plan.fecha.isoformat(), plan.cantidad)
            )
            plan.id = cursor.lastrowid
        return plan.id

    def get_all(self) -> List[Dict[str, Any]]:
        with self.tm.transaction() as conn:
            cursor = conn.execute("""
                SELECT pc.*, p.nombre as paciente_nombre, a.nombre as alimento_nombre, a.calorias
                FROM plan_comidas pc
                JOIN pacientes p ON pc.paciente_id = p.id
                JOIN alimentos a ON pc.alimento_id = a.id
                ORDER BY pc.fecha DESC;
            """)
            return [dict(row) for row in cursor.fetchall()]

    def get_by_paciente(self, paciente_id: int) -> List[Dict[str, Any]]:
        with self.tm.transaction() as conn:
            cursor = conn.execute("""
                SELECT pc.*, a.nombre as alimento_nombre, a.calorias
                FROM plan_comidas pc
                JOIN alimentos a ON pc.alimento_id = a.id
                WHERE pc.paciente_id = ?
                ORDER BY pc.fecha DESC;
            """, (paciente_id,))
            return [dict(row) for row in cursor.fetchall()]

    def get_by_id(self, plan_id: int) -> Optional[PlanComida]:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "SELECT * FROM plan_comidas WHERE id = ?;",
                (plan_id,)
            )
            row = cursor.fetchone()
            if row:
                row_dict = dict(row)
                row_dict['fecha'] = date.fromisoformat(row_dict['fecha'])
                return PlanComida(**row_dict)
            return None

    def delete(self, plan_id: int) -> bool:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "DELETE FROM plan_comidas WHERE id = ?;",
                (plan_id,)
            )
            return cursor.rowcount > 0

    def get_by_fecha(self, fecha: date) -> List[Dict[str, Any]]:
        with self.tm.transaction() as conn:
            cursor = conn.execute("""
                SELECT pc.*, p.nombre as paciente_nombre, a.nombre as alimento_nombre, a.calorias
                FROM plan_comidas pc
                JOIN pacientes p ON pc.paciente_id = p.id
                JOIN alimentos a ON pc.alimento_id = a.id
                WHERE pc.fecha = ?
                ORDER BY p.nombre;
            """, (fecha.isoformat(),))
            return [dict(row) for row in cursor.fetchall()]