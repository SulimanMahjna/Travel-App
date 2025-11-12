from src.places.model import places
from sqlalchemy import insert, select

def insert_place(data):
    return insert(places).values(**data)

def select_all_places():
    return select(places)

def select_place_by_id(place_id):
    return select(places).where(places.c.id == place_id)
