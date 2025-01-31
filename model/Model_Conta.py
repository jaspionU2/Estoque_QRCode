from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from configs.register import table_register


@table_register.mapped_as_dataclass
class Conta():
    __tablename__ = 'conta'
    
    id_conta: Mapped[int] = mapped_column(init=False, primary_key=True, name='id_conta')
    usuario_conta: Mapped[str] = mapped_column(String(200), nullable=False, name='usuario_conta', unique=True)
    email_conta: Mapped[str] = mapped_column(String(200), nullable=False, name='email_conta', unique=True)
    senha_conta: Mapped[str] = mapped_column(String(200), nullable=False, name='senha_conta')
    is_verifed_conta: Mapped[bool] = mapped_column(Boolean, nullable=False, name="is_verifed_conta", default=False)
    

