from sqlalchemy.orm import registry

table_register = registry()
metadata = table_register.metadata