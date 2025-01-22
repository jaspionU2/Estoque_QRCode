from sqlalchemy import String

from sqlalchemy.orm import (Mapped, mapped_column)

from configs.register import table_register
@table_register.mapped_as_dataclass
class Serie():
    __tablename__ = 'serie'
     
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_serie')
    Serie: Mapped[str] = mapped_column(String(20), name='titulo_serie', nullable=False)
