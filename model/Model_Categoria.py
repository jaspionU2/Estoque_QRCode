from sqlalchemy import String

from sqlalchemy.orm import (Mapped, mapped_column)

from configs.db_configs import table_register
@table_register.mapped_as_dataclass
class Categoria():
    __tablename__ = 'categoria'
     
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_categoria')
    categoria: Mapped[str] = mapped_column(String(20), name='titulo_categoria', nullable=False)
