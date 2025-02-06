from sqlalchemy import select, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from model.Model_Status import Status

from configs.db_configs import engine


class Status_CRUD:

    async def getAllStatus() -> bool | list:
        try:
            with Session(engine) as session:
                return session.execute(select(Status)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False

    async def createStatus(new_status: dict) -> bool | dict:
        try:
            with Session(engine) as session:

                result = session.execute(insert(Status).
                                         values(new_status).
                                         returning(Status.id, Status.status))
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

    async def deleteStatus(Id: int):
        try:
            with Session(engine) as session:

                result = session.execute(delete(Status).
                                         where(Status.id == Id))
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
