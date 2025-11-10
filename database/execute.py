from src.database.connection import engine

class DatabaseHandler:
    def execute_one(self, statement):
        with engine.begin() as connection:
            row = connection.execute(statement).fetchone()
            return row 

    def execute_all(self, statement):
        with engine.begin() as connection:
            row = connection.execute(statement).fetchall()
            return row 