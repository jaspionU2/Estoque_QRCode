from datetime import datetime
from sqlalchemy import (String, ForeignKey, TIMESTAMP)
from sqlalchemy.orm import (registry, Mapped, mapped_column)
from configs.register import table_register
@table_register.mapped_as_dataclass
class Emprestimo():
    __tablename__ = 'emprestimo'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_emprestimo')
    motivo_emprestimo: Mapped[str] = mapped_column(String(200), nullable=False, name='motivo_emprestimo')
    data_inicio_emprestimo: Mapped[datetime] = mapped_column(TIMESTAMP, name='data_inicio', nullable=False)
    data_fim_emprestimo: Mapped[datetime] = mapped_column(TIMESTAMP, name='data_fim', nullable=False)
    equipamento_emprestimo: Mapped[int] = mapped_column(ForeignKey('equipamento.id_equipamento'), name='id_equipamento')
    nome_usuario_emprestimo: Mapped[str] = mapped_column(String(100), name='nome_usuario')
    

