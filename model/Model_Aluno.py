import sqlalchemy

from sqlalchemy import (String, ForeignKey)
from sqlalchemy.orm import (Mapped, mapped_column)

from configs.register import table_register

@table_register.mapped_as_dataclass
class Aluno():
    __tablename__ = 'aluno'
    
    id: Mapped[int] = mapped_column(primary_key=True, init=False, name='id_aluno')
    nome: Mapped[str] = mapped_column(String(100), nullable=False, name='nome_aluno')
    serie: Mapped[int] = mapped_column(ForeignKey('serie.id_serie'), nullable=False, name='serie_aluno')
    turma: Mapped[str] = mapped_column(sqlalchemy.Enum('A', 'B', name='turma_enum'), nullable=False, name='turma_aluno')
    