from sqlalchemy import (String)
from sqlalchemy.orm import (Mapped, mapped_column)
from configs.db_configs import table_register

@table_register.mapped_as_dataclass
class Grupo():
    __tablename__ = 'grupo'
    
    id: Mapped[int] = mapped_column(name='id_grupo', init=False, primary_key=True)
    grupo: Mapped[str] = mapped_column(String(50), name='titulo_grupo', nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False, name='email_grupo', unique=True)