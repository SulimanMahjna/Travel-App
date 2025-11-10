from database_setup import users_table, todos_table, sub_todos_table
from datetime import datetime
from src.auth.query import TodoQueries

class TodoServices:
    def __init__(self):
        self.todo_query = TodoQueries()

    def get_all_user(self):
        rows = self.todo_query.get_all_user()
        if not rows:
            raise Exception("No users found")
        return rows

    def insert_user(self, user_data):
        row = self.todo_query.insert_user(user_data)
        if not row:
            raise Exception("Failed to insert user")
        return row

    def update_user(self, user_data):
        row = self.todo_query.update_user(user_data)
        if not row:
            raise Exception("Failed to update user")
        return row
