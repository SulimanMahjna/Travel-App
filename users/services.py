from src.database.execute import DatabaseHandler
from src.users.queries import insert_user, select_user_by_email
from werkzeug.security import generate_password_hash, check_password_hash

db = DatabaseHandler()

def register_user(data):
    data["password"] = generate_password_hash(data["password"])
    statement = insert_user(data)
    db.execute_commit(statement)
    return "User registered successfully"

def login_user(email, password):
    statement = select_user_by_email(email)
    user = db.execute_one(statement)
    if not user:
        return None
    if check_password_hash(user.password, password):
        return user
    return None