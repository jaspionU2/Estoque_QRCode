from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Materia import Materia

engine = create_engine(Config().DB_URI)


class Materia_CRUD:

    async def getAllMaterias():
        try:
            with Session(engine) as session:
                return session.execute(select(Materia)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False

    async def createMateria(new_materia: list[Materia]):
        try:
            with Session(engine) as session:

                materias = [materia_data.__dict__ for materia_data in new_materia]

                for materia in materias:
                    materia.pop("_sa_instance_state", None)

                result = session.execute(insert(Materia).
                                        values(materias))
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

    async def deleteMateria(Id: int):
        try:
            with Session(engine) as session:

                result = session.execute(delete(Materia).
                                        where(Materia.id == Id))
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
