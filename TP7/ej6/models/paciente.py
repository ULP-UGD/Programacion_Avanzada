from typing import Optional

class Paciente:
    def __init__(self, nombre: str, edad: int, peso: float, id: Optional[int] = None):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def __repr__(self):
        return (f"Paciente(id={self.id!r}, nombre={self.nombre!r}, edad={self.edad!r}, "
                f"peso={self.peso!r})")