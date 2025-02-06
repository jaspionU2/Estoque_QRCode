from sqlalchemy import create_engine

from sqlalchemy.orm import registry

from .settings import Config

table_register = registry()

engine = create_engine(Config().DB_URI)