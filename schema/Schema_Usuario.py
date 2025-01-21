from pydantic import BaseModel, Field, field_validator

from pydantic_core import PydanticCustomError

from enum import Enum

from typing import Generic, Literal
from typing_extensions import Annotated

from service.Serie_service import Serie_CRUD
from service.Materia_service import Materia_CRUD
from service.Usuarios_service import Professor_CRUD

class TurmaEnum(str, Enum):
    A = "A"
    B = "B"

class SchemaAluno(BaseModel):
    nome: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-Z\s]+$', examples=['Pablo Santana'])]
    serie: Annotated[int, Field(examples=[1, 2, 3])]
    turma: Annotated[TurmaEnum, Field(examples=['A', 'B'])]
    
    @field_validator('serie', mode='after')
    @classmethod
    def serie_existe_no_banco(cls, value: int):
        count_serie = len(Serie_CRUD.getAllSeries())
        
        if  value < 0 or value > count_serie:
            raise ValueError('A serie informada não existe')
        return value
    
class SchemaAlunoPublic(SchemaAluno):
    id: int
    
    
class SchemaProfessor(BaseModel):
    nome: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-Z\s]+$', examples=['Jose Pereira'])]
    
class SchemaProfessorPublic(SchemaProfessor):
    id: int
    
    
class SchemaProfessorMateria(BaseModel):
    professor: Annotated[int, Field(examples=[1, 2 , 3])]
    materia: Annotated[int, Field(examples=[1, 2 , 3])]
    
    @field_validator('professor', 'materia', mode='after')
    @classmethod
    def materia_professor_existe_no_banco(cls, value: int, info):
        count_materia = len(Materia_CRUD.getAllMaterias())
        count_Professor = len(Professor_CRUD.getAllProfessores())
        
        if info.field_name == 'materia':
            if  value < 1 or value > count_materia:
                raise PydanticCustomError(
                    'invalid value',
                    f'The value {value} is not valid for {info.field_name}. Must be between 1 and {count_materia}.'
                )
        elif info.field_name == 'professor':
             if  value < 1 or value > count_Professor:
                raise PydanticCustomError(
                    'invalid value',
                    f'The value {value} is not valid for {info.field_name}. Must be between 1 and {count_Professor}.'
                )
        return value