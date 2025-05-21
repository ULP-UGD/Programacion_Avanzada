from typing import List, Optional
from models import Paciente

class PacienteService:
    def __init__(self, paciente_repo):
        self.repo = paciente_repo

    def crear_paciente(self, nombre: str, edad: int, peso: float) -> Paciente:
        paciente = Paciente(nombre, edad, peso)
        paciente.id = self.repo.add(paciente)
        return paciente

    def obtener_todos(self) -> List[Paciente]:
        return self.repo.get_all()

    def obtener_por_id(self, paciente_id: int) -> Optional[Paciente]:
        return self.repo.get_by_id(paciente_id)

    def actualizar_paciente(self, paciente: Paciente) -> bool:
        return self.repo.update(paciente)

    def eliminar_paciente(self, paciente_id: int) -> bool:
        return self.repo.delete(paciente_id)

    def actualizar_peso(self, paciente_id: int, nuevo_peso: float) -> bool:
        paciente = self.obtener_por_id(paciente_id)
        if not paciente:
            return False
        paciente.peso_actual = nuevo_peso
        return self.actualizar_paciente(paciente)