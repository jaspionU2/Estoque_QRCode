from __future__ import annotations

from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict

from pydantic_core import PydanticCustomError

from typing_extensions import Annotated

from service.Usuarios_service import Usuario_Read
from service.Equipamento_service import Equipamento_CRUD



class SchemaStatus(BaseModel):
    status: Annotated[str, Field(min_length=3, max_length=20, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['QUEBRADO', 'STATUS'])]

class SchemaStatusPublico(SchemaStatus):
    id: int
    
    
class SchemaCategoria(BaseModel):
    categoria: Annotated[str, Field(min_length=3, max_length=20, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['CARREGADOR', 'CHROMEBOOK'])]

class SchemaCategoriaPublico(SchemaCategoria):
    id: int
    
    
class SchemaSerie(BaseModel):
    serie: Annotated[int, Field(gt=0, le=9, examples=[6, 7, 8])]
    
class SchemaSeriePublico(SchemaSerie):
    id: int
    

class SchemaMateria(BaseModel):
    materia: Annotated[str, Field(min_length=3, max_length=50, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['Historia', 'Geografia'])]
    
class SchemaMateriaPublico(SchemaMateria):
    id: int