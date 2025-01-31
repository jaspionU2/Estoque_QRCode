from sqlalchemy import select, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, OperationalError, IntegrityError
from model.Model_Materia import Materia
from configs.register import engine
from configs.CustomResponse import CustomResponse
class Materia_CRUD:

    def getAllMaterias() -> bool | list:
        try:
            with Session(engine) as session:
                return session.execute(select(Materia)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return CustomResponse(
                type_error=str(err.orig.__class__.__name__),
                sql_message=str(err.orig.diag.message_primary)
            )
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False

    def createMateria(new_materia: dict) -> bool | dict:
        try:
            with Session(engine) as session:


                result = session.execute(insert(Materia).
                                         values(new_materia).
                                         returning(Materia.id, Materia.materia))
                session.commit()

                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            
            return CustomResponse(
                type_error=str(err.orig.__class__.__name__),
                sql_message=str(err.orig.diag.message_primary)
            )
            
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False

    def deleteMateria(Id: int) -> bool:
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
            return False
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False
