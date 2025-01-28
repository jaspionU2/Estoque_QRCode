from __future__ import annotations

from pydantic import BaseModel, Field, field_validator, ValidationInfo, ConfigDict, EmailStr, SecretStr, field_serializer

from pydantic_core import PydanticCustomError

from typing import Optional
from typing_extensions import Annotated

from email_validator import validate_email, EmailNotValidError, caching_resolver

import re

class SchemaConta(BaseModel):    
    usuario_conta: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-ZÀ-ü\s\d_]+$', examples=['Clark Kent'])]
    email_conta: EmailStr
    senha_conta: SecretStr
    
    
    @field_validator('email_conta', mode='after')
    @classmethod
    def validated_email(cls, value):
        resolver = caching_resolver(timeout=10)
        
        try:
           validated_email = validate_email(value, check_deliverability=True, dns_resolver=resolver)
           
           return validated_email.ascii_email
        except EmailNotValidError as err:
            raise ValueError(f'invalid email adress: {err}')
        
    @field_validator('senha_conta', mode='before')
    @classmethod
    def validate_password(cls, value: str):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        if not re.fullmatch(pattern, value):
            raise PydanticCustomError(
                'invalid_value',
                'the password must contain at least 8 characters, including an uppercase letter, a  lowercase letter and a special character',
                {'pattern': pattern}
            ) 
        return SecretStr(value)  
        
    @field_serializer('senha_conta', when_used='json')
    def dump_password(cls, value: SecretStr):
        return value.get_secret_value()
        

class SchemaContaPublic(BaseModel):
    id_conta: int
    usuario_conta: str
    email_conta: EmailStr
