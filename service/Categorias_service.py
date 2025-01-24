from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Categoria import Categoria

from configs.register import engine


class Categoria_CRUD:

    async def getAllCategorias() -> bool | list:
        try:
            with Session(engine) as session:
                return session.execute(select(Categoria)).scalars().all()
        except SQLAlchemyError as err:
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            print(f"Erro inesperado: {err}")
            return False

    async def createCategoria(new_categoria: dict) -> dict | bool:
        try:
            with Session(engine) as session:
                result = session.execute(insert(Categoria).
                                         values(new_categoria).
                                         returning(Categoria.id, Categoria.categoria))
                session.commit()
                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False

    async def deleteCategoria(Id: int) -> bool:
        try:
            with Session(engine) as session:
                result = session.execute(delete(Categoria).where(Categoria.id == Id))
                session.commit()
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False
