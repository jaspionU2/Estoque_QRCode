from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from configs.settings import Config

from model.Model_Aluno import Aluno
from model.Model_Professor import Professor
from model.Model_Materia import Materia

engine = create_engine(Config().DB_URI)

class Aluno_CRUD():

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
            print("Erro inesperado: {err}")
            return False
    
    async def getAlunoById(Id: int) -> Aluno:
        try:
            with Session(engine) as session:
                return session.execute(
                    select(Aluno).
                    where(Aluno.id == Id)).scalar_one_or_none()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
        
    async def createAluno(new_aluno: Aluno) -> bool:
        try:
            with Session(engine) as session:
                # series = ["6", "7", "8", "9"]
                # turmas = ["A", "B", "C"]
                
                data = new_aluno.__dict__
                data.pop("_sa_instance_state", None)
                
                data["turma"] = new_aluno.turma.upper()
                
                # if not (data["serie"] in series) or not (data["turma"] in turmas):
                #     return False
                
                result = session.execute(insert(Aluno).values(data))
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
        
    async def updateAluno(Id: int, new_values: dict) -> bool:
        try:
            with Session(engine) as session:
                aluno = Aluno(**new_values)
                result = session.execute(update(Aluno).
                                where(Aluno.id == Id).
                                values(nome=aluno.nome,
                                    serie=aluno.serie,
                                    turma=aluno.turma))
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
            
    async def deleteAluno(Id: int) -> bool:
        try:
            with Session(engine) as session:
                result = session.execute(delete(Aluno).
                                where(Aluno.id == Id))
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
            
class Professor_CRUD:
    
    async def getAllProfessores() -> list[Professor]:
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
            print(err)
            return None
    
    async def getProfessorById(Id: int) -> Professor:
        try:
            with Session(engine) as session:
                return session.execute(
                    select(Professor).
                    where(Professor.id == Id)).scalar_one_or_none()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return None
            
    async def createProfessor(new_professor: dict) -> bool:
        try:
            with Session(engine) as session:
                session.execute(insert(Professor).
                                values(**new_professor))
                session.commit()
                return True
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return False
        except Exception as err:
            session.rollback()
            print(f"Erro inesperado: {err}")
            return False
        
    async def updateProfessor(Id: int, new_values: dict) -> bool:
        try:
            with Session(engine) as session:
                professor = Professor(**new_values)
                result = session.execute(update(Professor).
                                where(Professor.id == Id).
                                values(**new_values))
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
            
    async def deleteProfessor(Id: int) -> bool:
        try:
            with Session(engine) as session:
                result = session.execute(delete(Professor).
                                where(Professor.id == Id))
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