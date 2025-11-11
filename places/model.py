from sqlalchemy import Table, Column, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.database.connection import metadata
import uuid

places = Table(
    "places",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String),
    Column("descreption", Text),
    Column("location", Text),
    Column("features", Text),
    Column("created_at", TIMESTAMP, server_default=func.now()),
    Column("udated_at", TIMESTAMP, server_default=func.now())
)
