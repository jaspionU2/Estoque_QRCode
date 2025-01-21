from pydantic import BaseModel, Field, field_validator

from pydantic_core import PydanticCustomError

from enum import Enum

from typing import Generic, Literal
from typing_extensions import Annotated


class SchemaEquipamento(BaseModel):
    numero_serie_equipamento: Annotated[str, Field(pattern='^[\w\d]{15}$', examples=['Qwz803dftTp8MsC'])]
    matricula_equipamento: Annotated[str, Field(pattern='^[a-zA-Z][\w\d]{4}$', examples=['C0001', 'C0015'])]
    id_categoria_equipamento: Annotated[int, Field(examples=[1, 2, 3])]
    id_status_equipamento: Annotated[int, Field(examples=[1, 2, 3])]


class SchemaEquipamentoPublico(SchemaEquipamento):
    id_equipamento: int
    

class SchemaCarregador(BaseModel):
    matricula_carregador: Annotated[str, Field(pattern='^[a-zA-Z][\w\d]{4}$', examples=['C0001', 'C0015'])]
    id_status_carregador: Annotated[int, Field(examples=[1, 2, 3])]   

class SchemaCarregadorPublico(SchemaCarregador):
    id_carregador: int
    