from enum import Enum

from datetime import datetime

from typing import Literal, get_args

import sqlalchemy

from sqlalchemy import (String, INTEGER, func)
from sqlalchemy.orm import (registry, Mapped, mapped_column)

table_register = registry()

@table_register.mapped_as_dataclass
class Materia:
    __tablename__ = 'materia'
    
    materias = Literal[
        'PROTUGUES',
        'MATEMATICA',
        'FISICA',
        'CIENCIAS',
        'GEOGRAFIA',
        'FILOSOFIA',
        'INGLES',
        'HISTORIA',
        'ARTES',
        'PRODUCAO_TEXTO'
    ]
    
    # materias_lista = list(get_args(materias))

    id: Mapped[int] = mapped_column(name='id_materia', init=False, primary_key=True)
    materia: Mapped[Enum] = mapped_column(sqlalchemy.Enum(*materias), name='titulo_materia')
        