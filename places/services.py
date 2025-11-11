from src.database.execute import DatabaseHandler
from src.places.queries import insert_place, select_all_places

db = DatabaseHandler()

def add_place(data):
    statement = insert_place(data)
    db.execute_commit(statement)
    return "Place added successfully"

def get_all_places():
    statement = select_all_places()
    result = db.execute_all(statement)
    return [dict(row._mapping) for row in result]
