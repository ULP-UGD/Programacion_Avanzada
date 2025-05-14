from typing import List, Optional
from models import Alimento

class AlimentoRepository:
    def __init__(self, transaction_manager):
        self.tm = transaction_manager

    def add(self, alimento: Alimento) -> int:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "INSERT INTO alimentos (nombre, calorias) VALUES (?, ?);",
                (alimento.nombre, alimento.calorias)
            )
            alimento.id = cursor.lastrowid
        return alimento.id

    def get_all(self) -> List[Alimento]:
        with self.tm.transaction() as conn:
            cursor = conn.execute("SELECT * FROM alimentos;")
            return [Alimento(**dict(row)) for row in cursor.fetchall()]

    def get_by_id(self, alimento_id: int) -> Optional[Alimento]:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "SELECT * FROM alimentos WHERE id = ?;",
                (alimento_id,)
            )
            row = cursor.fetchone()
            return Alimento(**dict(row)) if row else None

    def update(self, alimento: Alimento) -> bool:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "UPDATE alimentos SET nombre = ?, calorias = ? WHERE id = ?;",
                (alimento.nombre, alimento.calorias, alimento.id)
            )
            return cursor.rowcount > 0

    def delete(self, alimento_id: int) -> bool:
        with self.tm.transaction() as conn:
            cursor = conn.execute(
                "DELETE FROM alimentos WHERE id = ?;",
                (alimento_id,)
            )
            return cursor.rowcount > 0