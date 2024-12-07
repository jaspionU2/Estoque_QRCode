from datetime import datetime

from typing import Literal


from sqlalchemy import ForeignKey
from sqlalchemy.orm import (registry, Mapped, mapped_column)

from model.Model_Usuario import Usuario
from model.Model_Equipamento import equipamento

register = registry()

@register.mapped_as_dataclass
class Atribuicao_permanente:
    __tablename__ = 'atribuicao_permanente'
    
    id: Mapped[int] = mapped_column(name='id_atribuicao_permanente',init=False, primary_key=True)
    usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id_usuario'),name='id_usuario')
    equipamento: Mapped[int] = mapped_column(ForeignKey('equipamento.id_equipamento'), name='id_equipamento')
    
    
    