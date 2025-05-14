from typing import List, Optional
from models import Alimento

class AlimentoService:
    def __init__(self, alimento_repo):
        self.repo = alimento_repo

    def crear_alimento(self, nombre: str, calorias: float) -> Alimento:
        alimento = Alimento(nombre, calorias)
        alimento.id = self.repo.add(alimento)
        return alimento

    def obtener_todos(self) -> List[Alimento]:
        return self.repo.get_all()

    def obtener_por_id(self, alimento_id: int) -> Optional[Alimento]:
        return self.repo.get_by_id(alimento_id)

    def actualizar_alimento(self, alimento: Alimento) -> bool:
        return self.repo.update(alimento)

    def eliminar_alimento(self, alimento_id: int) -> bool:
        return self.repo.delete(alimento_id)

    def buscar_por_nombre(self, nombre: str) -> List[Alimento]:
        todos = self.obtener_todos()
        return [a for a in todos if nombre.lower() in a.nombre.lower()]