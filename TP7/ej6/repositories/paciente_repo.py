from typing import List, Optional
from models import Paciente

class PacienteRepository:
    def __init__(self, transaction_manager):
        self.tm = transaction_manager

    def add(self, paciente: Paciente) -> int:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "INSERT INTO pacientes (nombre, edad, peso) VALUES (?, ?, ?);",
                (paciente.nombre, paciente.edad, paciente.peso)
            )
            paciente.id = cursor.lastrowid
        return paciente.id

    def get_all(self) -> List[Paciente]:
        with self.tm.transaction() as conn:
            cursor = conn.execute("SELECT * FROM pacientes;")
            return [Paciente(
                nombre=row['nombre'],
                edad=row['edad'],
                peso=row['peso'],
                id=row['id']
            ) for row in cursor.fetchall()]

    def get_by_id(self, paciente_id: int) -> Optional[Paciente]:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "SELECT * FROM pacientes WHERE id = ?;",
                (paciente_id,)
            )
            row = cursor.fetchone()
            if row:
                return Paciente(
                    nombre=row['nombre'],
                    edad=row['edad'],
                    peso=row['peso'],
                    id=row['id']
                )
            return None

    def update(self, paciente: Paciente) -> bool:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                """UPDATE pacientes 
                SET nombre = ?, edad = ?, peso = ? 
                WHERE id = ?;""",
                (paciente.nombre, paciente.edad, paciente.peso, paciente.id)
            )
            return cursor.rowcount > 0

    def delete(self, paciente_id: int) -> bool:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "DELETE FROM pacientes WHERE id = ?;",
                (paciente_id,)
            )
            return cursor.rowcount > 0