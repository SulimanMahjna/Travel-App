from sqlalchemy import create_engine, MetaData
import uuid
from datetime import datetime , timezone

engine = create_engine("postgresql+psycopg2://postgres:HATM@123@localhost:5432/mydatabase")
metadata = MetaData()
metadata.bind = engine

new_uuid = uuid.uuid4()
now = datetime.now(timezone("utc"))