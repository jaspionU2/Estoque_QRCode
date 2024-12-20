from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Categoria import Categoria

engine = create_engine(Config().DB_URI)


class Categoria_CRUD:

    async def getAllCategorias():
        try:
            with Session(engine) as session:
                return session.execute(select(Categoria)).scalars().all()
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            print("Erro inesperado: {err}")
            return None

    async def createCategoria(new_categoria: list[dict]):
        try:
            with Session(engine) as session:
                result = session.execute(insert(Categoria).
                                        values(new_categoria))
                session.commit()
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
    
    async def deleteCategoria(Id: int):
        try:
            with Session(engine) as session:
                result = session.execute(delete(Categoria).
                                where(Categoria.id == Id))
                session.commit()
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False     
