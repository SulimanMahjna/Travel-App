from database import users
from datetime import datetime
from src.database.execute import DatabaseHandler
from src.database.execute import DBClinet

class UserQueries:
    def __init__(self):
        self.db_client = DBClinet()

    def login(self, username, password):
        query = users.select().where(users.c.username == username)
        row = self.db_client.execute_one(query)
        if not row:
            return None, "no user have been found"
        return row
    
    def register(self, username, email , passowrd):
        query = users.insert().values(username = username, email=email, passowrd=passowrd)
        row = self.db_client.execute_one(query)
        if not row:
            return None, "user account creation issue"
        return row
