from sqlalchemy import Table, Column, String, Text, TIMESTAMP, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

metadata = MetaData()

places = Table(
    "places",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String(255), nullable=False),
    Column("description", Text),
    Column("location", Text),
    Column("features", Text),
    Column("created_at", TIMESTAMP, server_default=func.now()),
    Column("updated_at", TIMESTAMP, server_default=func.now(), onupdate=func.now()),
)
