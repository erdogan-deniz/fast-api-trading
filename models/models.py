from datetime import datetime
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

# The main metadata for working with migrations:
metadata = MetaData()

# Table roles:
roles = Table(
    "roles",  # Название таблицы
    metadata,  # Метаданные для изменения

    # Описание коломок таблицы:
    Column("permit", JSON),
    Column("name", String, nullable=False),
    Column("id", Integer, primary_key=True)
)

# Table users:
users = Table(
    "users",  # Название таблицы
    metadata,  # Метаданные для изменения

    # Описание коломок таблицы:
    Column("id", Integer, primary_key=True),
    Column("e-mail", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow)
)
