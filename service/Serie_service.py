from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_serie import Serie

from configs.register import engine


class Serie_CRUD:

    def getAllSeries():
        try:
            with Session(engine) as session:
                return session.execute(select(Serie)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False

    def createSerie(new_materia: list[Serie]):
        try:
            with Session(engine) as session:

                series = [serie_data.__dict__ for serie_data in new_materia]

                for serie in series:
                    serie.pop("_sa_instance_state", None)

                result = session.execute(insert(Serie).values(series))
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

    def deleteSerie(Id: int):
        try:
            with Session(engine) as session:

                result = session.execute(delete(Serie).where(Serie.id == Id))
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
