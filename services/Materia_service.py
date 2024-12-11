from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Materia import Materia

engine = create_engine(Config().DB_URI)


class Materia_CRUD:

    async def getAllMaterias():

        with Session(engine) as session:

            return session.execute(select(Materia)).scalars().all()

    async def createMateria(new_materia: list[Materia]):

        with Session(engine) as session:

            materias = [materia_data.__dict__ for materia_data in new_materia]

            for materia in materias:
                materia.pop("_sa_instance_state", None)

            result = session.execute(insert(Materia).
                                     values(materias))
            session.commit()

            return result.rowcount

    async def deleteMateria(Id: int):

        with Session(engine) as session:

            result = session.execute(delete(Materia).
                                     where(Materia.id == Id))
            session.commit()

            return result.rowcount
