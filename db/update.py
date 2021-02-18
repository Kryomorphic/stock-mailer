from db.models.Base import Base
from db.access import mysql_engine


def update_schema():
    Base.metadata.create_all(mysql_engine)
