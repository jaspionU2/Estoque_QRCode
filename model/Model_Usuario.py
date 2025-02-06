from sqlalchemy import ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import (Mapped, mapped_column)
import sqlalchemy

from configs.db_configs import table_register
@table_register.mapped_as_dataclass
class Usuario():
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_usuario')
    aluno: Mapped[int] = mapped_column(ForeignKey('aluno.id_aluno'), name='id_aluno')
    professor: Mapped[int] = mapped_column(ForeignKey('professor.id_professor'), name='id_professor')
    tipo_usuario: Mapped[str] = mapped_column(sqlalchemy.Enum('ALUNO', 'PROFESSOR', name='tipo_usuario_enum'), nullable=False, name='tipo_usuario')
    
    __table_args__ = (
        CheckConstraint(
            "((id_aluno = NULL) AND (id_professor <> NULL)) OR ((id_aluno <> NULL) AND (id_professor = NULL))",
            name='check_usuario'
        ),
    )
    
