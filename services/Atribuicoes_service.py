from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Atribuicao_permanente import Atribuicao_permanente as Atribuicao

engine = create_engine(Config().DB_URI)

class Atribuicao_CRUD:
    async def getAllAtrubuicoes():
        try:
            with Session(engine) as session:
                return None
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            print("Erro inesperado: {err}")
            return None