from sqlalchemy import create_engine, select, update, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Aluno import Aluno
from model.Model_Professor import Professor

engine = create_engine(Config().DB_URI)

class Aluno_CRUD():

    async def getAllAlunos():
        
        with Session(engine) as session:
                    
            return session.execute(select(Aluno)).scalars().all()
    
    async def getAlunoById(Id: int):
        
        with Session(engine) as session:
            
            return session.execute(
                select(Aluno).
                where(Aluno.id == Id)).scalar_one_or_none()
        
    async def createAluno(new_aluno: list[dict]):
        
            with Session(engine) as session:
                
                result = session.execute(insert(Aluno).
                                values(new_aluno))
                session.commit()
                return result.rowcount

        
    async def updateAluno(Id: int, new_values: dict):
        
        with Session(engine) as session:
        
            aluno = Aluno(**new_values)
            
            session.execute(update(Aluno).
                            where(Aluno.id == Id).
                            values(nome=aluno.nome,
                                serie=aluno.serie,
                                turma=aluno.turma))
            
            session.commit()
            
    async def deleteAluno(Id: int):
        
        with Session(engine) as session:
            
            session.execute(delete(Aluno).
                            where(Aluno.id == Id))
            session.commit()
            
class Professor_CRUD:
    
    async def getAllProfessores():
        
        with Session(engine) as session:
                    
            return session.execute(select(Professor)).scalars().all()
    
    async def getProfessorById(Id: int):
        
        with Session(engine) as session:
            
            return session.execute(
                select(Professor).
                where(Professor.id == Id)).scalar_one_or_none()
            
    async def createProfessor(new_professor: list[dict]) -> bool:
       
            with Session(engine) as session:
                
                result = session.execute(insert(Professor).
                                values(new_professor))
                session.commit()
                return result.rowcount
        
    async def updateProfessor(Id: int, new_values: dict):
        
        with Session(engine) as session:
        
            professor = Professor(**new_values)
            
            session.execute(update(Professor).
                            where(Professor.id == Id).
                            values(nome=professor.nome))
            
            session.commit()
            
    async def deleteProfessor(Id: int):
        
        with Session(engine) as session:
            
            session.execute(delete(Professor).
                            where(Professor.id == Id))
            
            session.commit()