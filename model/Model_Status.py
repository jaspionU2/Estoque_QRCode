from sqlalchemy import String
from sqlalchemy.orm import (registry, Mapped, mapped_column, relationship)
from configs.register import table_register, metadata

@table_register.mapped_as_dataclass
class Status():
    __tablename__ = 'status'
    
    id: Mapped[int] = mapped_column(name='id_status', init=False, primary_key=True)
    status: Mapped[str] = mapped_column(String(20), name='titulo_status')
    
