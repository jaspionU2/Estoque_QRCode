from enum import Enum

from datetime import datetime

import sqlalchemy

from sqlalchemy import (String, func)
from sqlalchemy.orm import (registry, Mapped, mapped_column)

from configs.register import table_register
@table_register.mapped_as_dataclass
class Aluno():
    __tablename__ = 'aluno'
    
    id: Mapped[int] = mapped_column(primary_key=True, init=False, name='id_aluno')
    nome: Mapped[str] = mapped_column(String(100), nullable=False, name='nome_aluno')
    serie: Mapped[Enum] = mapped_column(sqlalchemy.Enum('6', '7', '8', '9', name='serie_enum'), nullable=False, name='serie_aluno')
    turma: Mapped[Enum] = mapped_column(sqlalchemy.Enum('A', 'B', name='turma_enum'), nullable=False, name='turma_aluno')
    created_at: Mapped[datetime] = mapped_column(name='created_at', server_default=func.now())
    