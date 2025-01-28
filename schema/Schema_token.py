from pydantic import BaseModel

class TokenPublic(BaseModel):
    access_token: str
    type_token: str