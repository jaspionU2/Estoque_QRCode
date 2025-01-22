from sqlalchemy import ForeignKey
from sqlalchemy.orm import (registry, Mapped, mapped_column)
from model.Model_Aluno import Aluno
from model.Model_Professor import Professor
from configs.register import table_register
@table_register.mapped_as_dataclass
class Usuario():
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_usuario')
    aluno: Mapped[int] = mapped_column(ForeignKey('aluno.id_aluno'), name='id_aluno')
    professor: Mapped[int] = mapped_column(ForeignKey('professor.id_professor'), name='id_professor')
