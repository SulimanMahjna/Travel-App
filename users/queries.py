from src.users.model import users
from sqlalchemy import insert, select

def insert_user(data):
    return insert(users).values(**data)

def select_user_by_email(email):
    return select(users).where(users.c.email == email)

def select_user_by_username(username):
    return select(users).where(users.c.username == username)