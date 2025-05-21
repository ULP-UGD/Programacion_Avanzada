from datetime import date
from typing import Optional

class PlanComida:
    def __init__(self, paciente_id: int, alimento_id: int, fecha: date, 
                 cantidad: float, plan_id: Optional[int] = None):
        self.id = plan_id
        self.paciente_id = paciente_id
        self.alimento_id = alimento_id
        self.fecha = fecha
        self.cantidad = cantidad
    
    def __repr__(self):
        return (f"PlanComida(id={self.id!r}, paciente_id={self.paciente_id!r}, "
                f"alimento_id={self.alimento_id!r}, fecha={self.fecha!r}, "
                f"cantidad={self.cantidad!r})")