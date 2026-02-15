from __future__ import annotations

from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict, EmailStr, SecretStr

from pydantic_core import PydanticCustomError

from datetime import date, datetime

from typing import Optional
from typing_extensions import Annotated

from service.Usuarios_service import Usuario_Read
from service.Equipamento_service import Equipamento_CRUD


class SchemaConta(BaseModel):
    usuario_conta: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['Clark Kent'])]
    email_conta: EmailStr
    senha_conta: SecretStr

class SchemaConta(BaseModel):
    id_conta: int
    usuario_conta: str
    email_conta: EmailStr
    