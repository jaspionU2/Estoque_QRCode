from pydantic_settings import (BaseSettings, SettingsConfigDict)

class Config(BaseSettings):
    
    model_config = SettingsConfigDict (
        env_file='/.env',
        env_file_encoding='utf8'
    )
    
    DB_URI: str
    
    
    
    