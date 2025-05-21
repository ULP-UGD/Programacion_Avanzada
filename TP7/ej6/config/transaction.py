import sqlite3
from contextlib import contextmanager
from typing import Iterator, Optional, Any

class TransactionManager:
    def __init__(self, db_config: Any):
        self.db_config = db_config
        self.connection: Optional[sqlite3.Connection] = None

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        """Proporciona un contexto transaccional con manejo automático de commit/rollback"""
        conn = self.db_config.get_connection()
        self.connection = conn
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()
            self.connection = None

    def get_current_connection(self) -> sqlite3.Connection:
        """Obtiene la conexión activa en una transacción"""
        if not self.connection:
            raise RuntimeError("No hay transacción activa")
        return self.connection