from enum import Enum
from sqlalchemy import (String)
from sqlalchemy.orm import (registry, Mapped, mapped_column)
from configs.register import table_register
@table_register.mapped_as_dataclass
class Materia():
    __tablename__ = 'materia'
    
    id: Mapped[int] = mapped_column(name='id_materia', init=False, primary_key=True)
    materia: Mapped[str] = mapped_column(String(50), name='titulo_materia', nullable=False)
        
metadata = table_register.metadata