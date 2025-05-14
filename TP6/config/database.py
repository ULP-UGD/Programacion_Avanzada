import sqlite3

class DatabaseConfig:
    def __init__(self, db_path: str = "TP6/nutricionista.db"):
        self.db_path = db_path
        self._initialize_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")  # Habilita claves foraneas
        return conn

    def _initialize_db(self):
        sqls = [
            """
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                peso REAL NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS alimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                calorias REAL NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS plan_comidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                alimento_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                cantidad REAL NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE,
                FOREIGN KEY (alimento_id) REFERENCES alimentos(id) ON DELETE RESTRICT
            );
            """
        ]

        with self.get_connection() as conn:
            for sql in sqls:
                conn.execute(sql)