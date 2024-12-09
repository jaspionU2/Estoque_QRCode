from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from configs.settings import Config
from configs.register import metadata
from model.Model_Aluno import Aluno

engine = create_engine("postgresql+psycopg2://postgres:220206@localhost:5432/estoquemirim")


async def getAllAlunos():
    
    with Session(engine) as session:
                
      return session.execute(select(Aluno)).scalars().all()
  
async def getAlunoById(Id: int):
    
    with Session(engine) as session:
        
      return session.execute(
          select(Aluno).
          where(Aluno.id == Id)).scalar_one_or_none()
      
async def createAluno(new_aluno: dict):
    
    try:
        with Session(engine) as session:
            
            aluno = Aluno(**new_aluno)
            
            session.add(aluno)  
            
            session.commit()
            
            return True
    except:
        return False
    
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