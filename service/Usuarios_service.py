from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from configs.settings import Config

from model.Model_Aluno import Aluno
from model.Model_Professor import Professor
from model.Model_Usuario import Usuario

from configs.register import engine


class Usuario_Read():

    async def getAllUsuarios() -> list:
            try:
                with Session(engine) as session:
                    return session.execute(select(Usuario)).scalars().all()
            except SQLAlchemyError as err:
                session.rollback()
                print(err._message())
                print(err._sql_message())
                return None
            except Exception as err:
                session.rollback()
                print(f"Erro inesperado: {err}")
                return None

class Aluno_CRUD:
    

    async def getAllAlunos() -> list:
        try:
            with Session(engine) as session:
                return session.execute(select(Aluno)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def getAlunoById(Id: int) -> list:
        try:
            with Session(engine) as session:
                return session.execute(
                    select(Aluno).where(Aluno.id == Id)
                ).fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def createAluno(new_aluno: dict) -> dict:
        try:
            with Session(engine) as session:
                result = session.execute(
                    insert(Aluno)
                    .values(new_aluno)
                    .returning(Aluno.id, Aluno.nome, Aluno.serie, Aluno.turma)
                )
                session.commit()

                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def updateAluno(Id: int, new_values: dict) -> dict:
        try:
            with Session(engine) as session:
                result = session.execute(
                    update(Aluno)
                    .where(Aluno.id == Id)
                    .values(new_values)
                    .returning(Aluno.id, Aluno.nome, Aluno.serie, Aluno.turma)
                )
                session.commit()
                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def deleteAluno(Id: int) -> bool:
        try:
            with Session(engine) as session:
                result = session.execute(delete(Aluno).where(Aluno.id == Id))
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


class Professor_CRUD:

    async def getAllProfessores() -> list:
        try:
            with Session(engine) as session:
                return session.execute(select(Professor)).all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def getProfessorById(Id: int) -> list:
        try:
            with Session(engine) as session:
                return session.execute(
                    select(Professor).where(Professor.id == Id)
                ).scalar_one_or_none()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def createProfessor(new_professor: dict) -> dict:
        try:
            with Session(engine) as session:
                result = session.execute(
                    insert(Professor)
                    .values(new_professor)
                    .returning(Professor.id, Professor.nome)
                )
                session.commit()
                return result.fetchone()._asdict()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return None

    async def updateProfessor(Id: int, new_values: dict) -> dict:
        try:
            with Session(engine) as session:
                result = session.execute(
                    update(Professor).where(Professor.id == Id).values(new_values)
                )
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
            return None

    async def deleteProfessor(Id: int) -> bool:
        try:
            with Session(engine) as session:
                result = session.execute(delete(Professor).where(Professor.id == Id))
                session.commit()
                return result.rowcount > 0
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
