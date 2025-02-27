from __future__ import annotations

from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict

from pydantic_core import PydanticCustomError

from datetime import date, datetime

from typing import Optional
from typing_extensions import Annotated

from service.Usuarios_service import Usuario_Read
from service.Equipamento_service import Equipamento_CRUD


class SchemaEmprestimo(BaseModel):
    motivo_emprestimo: Annotated[Optional[str], Field(max_length=200, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['O funcionaro x requisitou uso do equipamento para trabalho'], default=None)]
    data_inicio_emprestimo: Annotated[date, Field(examples=['2025-05-13'])]
    data_fim_emprestimo: Annotated[date, Field(examples=['2025-05-17'])]
    equipamento_emprestimo: Annotated[int, Field(examples=[1, 2, 3])]
    nome_usuario_emprestimo: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['Carlos Roberto Pereira'])]

    @field_validator('data_inicio_emprestimo', 'data_fim_emprestimo', mode='after')
    @classmethod
    def string_to_date(cls, values):
        if isinstance(values, str):
            return datetime.strptime(values, '%Y-%m-%d').date()
        return values
    
    @field_validator('data_inicio_emprestimo', 'data_fim_emprestimo', mode='after')
    @classmethod
    def date_today_or_later(cls, values):
        if values < date.today():
            raise PydanticCustomError(
                'invalid value',
                f'the data {values} given is later than today. the date must {date.today()} or later',
                {'invalid_date': values, 'minimum_date': date.today()}
               )
        return values
    
    @field_validator('data_fim_emprestimo', mode='after')
    @classmethod
    def date_end_must_greather_than_date_start(cls, values, info: ValidationInfo):
        data = info.data.get('data_inicio_emprestimo')
        if values < data:
            raise PydanticCustomError(
                'invalid value',
                f'the data {values} given is later than the date start {data}. the date must {data} or later',
                {'invalid_date': values, 'minimum_date': data}
               )
        return values
            
class SchemaEmprestimoPublico(SchemaEmprestimo):
    id: int


class SchemaAtribuicao(BaseModel):
    usuario: Annotated[int, Field(examples=[1, 2, 3])]
    equipamento: Annotated[int, Field(examples=[1, 2, 3])]
    
    @field_validator('usuario', 'equipamento', mode='after')
    @classmethod
    def materia_professor_existe_no_banco(cls, value: int, info):
        count_usuario = len(Usuario_Read.getAllUsuarios())
        count_equipamento = len(Equipamento_CRUD.getAllEquipamentos())
        
        if info.field_name == 'usuario':
            if  value < 1 or value > count_usuario:
                raise PydanticCustomError(
                    'invalid value',
                    f'The value {value} is not valid for {info.field_name}. Must be between 1 and {count_usuario}.'
                )
        elif info.field_name == 'equipamento':
             if  value < 1 or value > count_equipamento:
                raise PydanticCustomError(
                    'invalid value',
                    f'The value {value} is not valid for {info.field_name}. Must be between 1 and {count_equipamento}.'
                )
        return value

class SchemaAtribuicaoPublico(SchemaAtribuicao):
    id: int
        
        