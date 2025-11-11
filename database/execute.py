from src.database.connection import engine

class DatabaseHandler:
    def execute_one(self, statement):
        with engine.begin() as connection:
            result = connection.execute(statement).fetchone()
            return result

    def execute_all(self, statement):
        with engine.begin() as connection:
            result = connection.execute(statement).fetchall()
            return result

