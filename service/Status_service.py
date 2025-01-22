from sqlalchemy import create_engine, select, delete, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from configs.settings import Config
from model.Model_Status import Status

engine = create_engine(Config().DB_URI)

class Status_CRUD:
    
    async def getAllStatus():
        try:
            with Session(engine) as session:
                return session.execute(select(Status)).scalars().all()
        except SQLAlchemyError as err:
            session.rollback()
            print(err._message())
            print(err._sql_message())
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
       
    async def createStatus(new_status: list[dict]):
        try:
            with Session(engine) as session:
                
                result = session.execute(insert(Status).
                                values(new_status))
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
            return None
        except Exception as err:
            session.rollback()
            print("Erro inesperado: {err}")
            return False
        
    
            
            
    
    