from sqlalchemy import (String, ForeignKey)
from sqlalchemy.orm import (registry, Mapped, mapped_column,)
from configs.register import table_register
@table_register.mapped_as_dataclass
class Equipamento():
    __tablename__ = 'equipamento'
    
    id_equipamento: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_equipamento') 
    numero_serie_equipamento: Mapped[str] = mapped_column(String(15), nullable=True, name='numero_de_serie')
    matricula_equipamento: Mapped[str] = mapped_column(String(5), nullable=False, name='matricula_equipamento')
    id_categoria_equipamento: Mapped[int] = mapped_column(ForeignKey('categoria.id_categoria'), name='id_categoria')
    id_status_equipamento: Mapped[int] = mapped_column(ForeignKey('status.id_status'), name='id_status')
    
    categoria_equipamento: str
    status_equipamento: str

metadata = table_register.metadata