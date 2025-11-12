from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql+psycopg2://postgres:HATM@123@localhost:5432/mydatabase")

metadata = MetaData()
metadata.bind = engine