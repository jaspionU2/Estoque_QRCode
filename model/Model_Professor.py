from datetime import datetime
from sqlalchemy import (String)
from sqlalchemy.orm import (registry, Mapped, mapped_column, relationship)
from configs.register import table_register
@table_register.mapped_as_dataclass
class Professor():
    __tablename__ = 'professor'
    
    id: Mapped[int] = mapped_column(name='id_professor', init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), name='nome_professor', nullable=False)

    
