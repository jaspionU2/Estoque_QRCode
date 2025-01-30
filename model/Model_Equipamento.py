from sqlalchemy import (String, ForeignKey)
from sqlalchemy.orm import (Mapped, mapped_column,)
from configs.register import table_register
@table_register.mapped_as_dataclass
class Equipamento():
    __tablename__ = 'equipamento'
    
    id_equipamento: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_equipamento') 
    numero_serie_equipamento: Mapped[str] = mapped_column(String(15), nullable=True, name='numero_de_serie', unique=True)
    matricula_equipamento: Mapped[str] = mapped_column(String(5), nullable=False, name='matricula_equipamento', unique=True)
    id_categoria_equipamento: Mapped[int] = mapped_column(ForeignKey('categoria.id_categoria'), name='id_categoria')
    id_status_equipamento: Mapped[int] = mapped_column(ForeignKey('status.id_status'), name='id_status')
    id_carregador: Mapped[int] = mapped_column(ForeignKey('carrregador.id_carregador'), name='id_carregador')

