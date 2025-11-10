from sqlalchemy import MetaData, Table, Column, Integer, String, Datetime

user= Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("email", String(100), unique=True),
    Column("password", String(100), unique=True),
    Column("created_at", Datetime),
    Column("updated_at", Datetime)
)

todo= Table(
    "todo", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("description", String(100), unique=True),
    Column("datetime", Datetime),
    Column("created_at", Datetime),
    Column("updated_at", Datetime),
)