from sqlalchemy import ForeignKey
from sqlalchemy.orm import (registry, Mapped, mapped_column)
from configs.db_configs import table_register

@table_register.mapped_as_dataclass
class ProfessorMateria():
    __tablename__ = 'professor_materia'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_professor_materia')
    professor: Mapped[int] = mapped_column(ForeignKey('professor.id_professor'), name='id_professor')
    materia: Mapped[int] = mapped_column(ForeignKey('materia.id_materia'), name='id_materia')
