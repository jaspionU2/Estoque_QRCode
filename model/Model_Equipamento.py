from sqlalchemy import (String, ForeignKey)
from sqlalchemy.orm import (registry, Mapped, mapped_column,)
from configs.register import table_register
@table_register.mapped_as_dataclass
class Equipamento():
    __tablename__ = 'equipamento'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_equipamento')
    numero_serie: Mapped[str] = mapped_column(String(15), nullable=True, name='numero_de_serie')
    matricula: Mapped[str] = mapped_column(String(5), nullable=False, name='matricula_equipamento')
    categoria: Mapped[int] = mapped_column(ForeignKey('categoria.id_categoria'), name='id_categoria')
    status: Mapped[int] = mapped_column(ForeignKey('status.id_status'), name='id_status')

metadata = table_register.metadata