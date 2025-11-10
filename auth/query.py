from database_setup import users_table, todos_table, sub_todos_table
from datetime import datetime
from src.database.execute import DatabaseHandler

class TodoQueries:
    def __init__(self):
        self.db_client = DatabaseHandler()

    def get_all_user(self):
        query = users_table.select()
        rows = self.db_client.get_all_todo(query)
        if not rows:
            raise Exception("No users found.")
        return rows

    def insert_user(self, user_data):
        query = users_table.insert().values(user_data).returning(users_table)
        row = self.db_client.insert_todo(query)
        return row

    def update_user(self, user_data):
        query = users_table.update().values(user_data).returning(users_table)
        row = self.db_client.update_todo(query)
        return row
