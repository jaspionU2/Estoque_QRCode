from enum import Enum

from datetime import datetime

from typing import Literal

import sqlalchemy

from sqlalchemy import (String, INTEGER)
from sqlalchemy.orm import (registry, Mapped, mapped_column)

table_register = registry()

class Serie(Enum):
    SEIS = '6'
    SETE = '7'
    OITO = '8'
    NOVE = '9'

class Turma(Enum):
    A = "A"
    B = "B"

# Registro do mapeamento
table_register = registry()

@table_register.mapped_as_dataclass
class Aluno:
    __tablename__ = 'aluno'
    
    id: Mapped[int] = mapped_column(primary_key=True, init=False, name='id_aluno')
    nome: Mapped[str] = mapped_column(String(100), nullable=False, name='nome_aluno')
    serie: Mapped[Enum] = mapped_column(sqlalchemy.Enum('6', '7', '8', '9'), nullable=False, name='serie_aluno')
    turma: Mapped[Enum] = mapped_column(sqlalchemy.Enum('A', 'B'), nullable=False, name='turma_aluno')