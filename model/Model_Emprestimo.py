import sqlalchemy

from datetime import datetime

from sqlalchemy import (String, ForeignKey)
    
from sqlalchemy.orm import (registry, Mapped, mapped_column)

from model.Model_Equipamento import Equipamento

table_register = registry()

@table_register.mapped_as_dataclass
class Emprestimo:
    _tablename__ = 'emprestimo'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_emprestimo')
    motivo_emprestimo: Mapped[str] = mapped_column(String(200), nullable=False, name='motivo_emprestimo')
    data_inicio: Mapped[datetime] = mapped_column(sqlalchemy.DATETIME(), name='data_inicio', nullable=False)
    data_fim: Mapped[datetime] = mapped_column(sqlalchemy.DATETIME(), name='data_fim', nullable=False)
    equipamento: Mapped[int] = mapped_column(ForeignKey('equipamento.id_equipamento'), name='id_equipamento')
    nome_usuario: Mapped[str] = mapped_column(String(100), name='nome_usuario')
