from sqlalchemy import (String, ForeignKey)
from sqlalchemy.orm import (registry, Mapped, mapped_column, relationship)
from configs.register import table_register, metadata

@table_register.mapped_as_dataclass
class Carregador():
    __tablename__ = 'carregador'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_carregador')
    matricula: Mapped[str] = mapped_column(String(5), name='matricula_carregador', nullable=False, unique=True)
    id_status: Mapped[int] = mapped_column(ForeignKey('status.id_status'), name='id_status')
    

