from typing import Optional

class Alimento:
    def __init__(self, nombre: str, calorias: float, id: Optional[int] = None):
        self.id = id
        self.nombre = nombre
        self.calorias = calorias

    def __repr__(self):
        return f"Alimento(id={self.id!r}, nombre={self.nombre!r}, calorias={self.calorias!r})"